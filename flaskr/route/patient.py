from flask import Blueprint, request, jsonify
from model import patient
from dateutil import parser
from werkzeug.exceptions import HTTPException

patient_api = Blueprint('patient_api', __name__, url_prefix='/api')

@patient_api.route('/patient', methods=('GET', 'POST'))
def patient_route():
    if request.method == 'GET':
        patient_id = request.args.get('id')
        return jsonify(patient.getPatient(patient_id=patient_id))
    elif request.method == 'POST':
        try:
            params = {}
            params['firstname']=request.form['firstname']
            params['lastname']=request.form['lastname']
            params['sex']=request.form['sex']
            params['birthdate']=parser.parse(request.form['birthdate']).strftime('%Y-%m-%d')
            params['address']=request.form['address']
            params['phone']=request.form['phone']
            params['parent_firstname']=request.form['parent_firstname']
            params['parent_lastname']=request.form['parent_lastname']
            params['parent_phone']=request.form['parent_phone']
            if 'allergy' in request.form:
                params['allergy']=request.form['allergy'].split(',')
            patient.insertPatient(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception:
            return '' , 500

@patient_api.route('/patient/<patient_id>', methods=('GET',))
def patient_id_route(patient_id):
    if request.method == 'GET':
        return jsonify(patient.getPatient(patient_id=patient_id))
