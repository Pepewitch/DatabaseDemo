from flask import Blueprint, request, jsonify
from model import treatment
from dateutil import parser
from werkzeug.exceptions import HTTPException

treatment_api = Blueprint('treatment_api', __name__, url_prefix='/api')

@treatment_api.route('/treatment', methods=('GET', 'POST'))
def treatment_route():
    if request.method == 'GET':
        try:
            params = {
                'patient_id' : request.args.get('patient_id'),
                'doctor_id' : request.args.get('doctor_id')
            }
            return jsonify(treatment.getTreatment(**params))
        except Exception:
            return '' , 500
        
    elif request.method == 'POST':
        try:
            params = {
                'doctor_id': request.form['doctor_id'] , 
                'patient_id': request.form['patient_id'] , 
                'cost': request.form['cost'],
                'symptom': request.form['symptom'],
            }
            treatment.insertTreatment(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            return '' , 500

@treatment_api.route('/treatment/<treatment_id>', methods=('PATCH','DELETE'))
def treatment_id_route(treatment_id):
    if request.method == 'PATCH':
        try:
            params = {
                'doctor_id': doctor_id,
                'patient_id': patient_id,
            }
            if 'doctor_id' in request.form:
                params['doctor_id'] = request.form['doctor_id']
            if 'patient_id' in request.form:
                params['patient_id'] = request.form['patient_id']
            if 'cost' in request.form: 
                param['cost'] = request.form['cost']
            if 'symptom' in request.form: 
                param['symptom'] = request.form['symptom']
            treatment.updateTreatment(**params)
            return '' , 200
        except HTTPException:
            return '' , 400
        except Exception:
            return '' , 500
    if request.method == 'DELETE':
        try:
            treatment.deleteTreatment(treatment_id)
            return '', 200
        except Exception:
           return '', 500 
