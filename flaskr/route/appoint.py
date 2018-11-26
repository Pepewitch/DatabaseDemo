from flask import Blueprint, request, jsonify
from model import staff, department, patient, appoint
from dateutil import parser
from werkzeug.exceptions import HTTPException

appoint_api = Blueprint('appoint_api', __name__, url_prefix='/api')

@appoint_api.route('/appoint', methods=('GET', 'POST'))
def appoint_route():
    if request.method == 'GET':
        try:
            params = {
                'patient_id' : request.args.get('patient_id'),
                'doctor_id' : request.args.get('doctor_id')
            }
            return jsonify(appoint.getAppoint(**params))
        except Exception:
            return '' , 500
        
    elif request.method == 'POST':
        try:
            params = {
                'doctor_id':request.form['doctor_id'] , 
                'patient_id':request.form['patient_id'] , 
                'appoint_date':parser.parse(request.form['appoint_date']).strftime('%Y-%m-%d %H:%M:%S')
            }
            appoint.insertAppoint(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            return '' , 500

@appoint_api.route('/appoint/<appoint_id>', methods=('PATCH','DELETE'))
def appoint_id_route(appoint_id):
    if request.method == 'PATCH':
        try:
            params = {
                'appoint_id': appoint_id
            }
            if 'doctor_id' in request.form:
                params['doctor_id'] = request.form['doctor_id']
            if 'patient_id' in request.form:
                params['patient_id'] = request.form['patient_id']
            if 'appoint_date' in request.form: 
                params['appoint_date'] = parser.parse(request.form['appoint_date']).strftime('%Y-%m-%d %H:%M:%S')
            appoint.updateAppointment(**params)
            return '' , 200
        except HTTPException:
            return '' , 400
        except Exception:
            return '' , 500
    if request.method == 'DELETE':
        try:
            appoint.deleteAppoint(appoint_id)
            return '', 200
        except Exception:
           return '', 500 
