from flask import Blueprint, request, jsonify
from model import staff, department, patient, appoint
from dateutil import parser
from werkzeug.exceptions import HTTPException, NotFound

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/medical_staff' , methods=('GET',))
def medical_staff_route():
    try:
        params = {
            'medical_type' : request.args.get('type'),
            'staff_id' : request.args.get('id')
        }
        return jsonify(staff.getMedicalStaff(**params))
    except Exception:
        return '' , 500

@api.route('/medical_staff/<staff_id>' , methods=('GET' , 'PATCH' , 'DELETE'))
def medical_staff_id_route(staff_id):
    if request.method == 'GET':
        try:
            params = {
            'medical_type' : request.args.get('type'),
            'staff_id' : staff_id
            }
            return jsonify(staff.getMedicalStaff(**params))
        except Exception:
            return '' , 500
    elif request.method == 'PATCH':
        try:
            params = { 'staff_id' : staff_id }
            keys = ['sex' , 'salary' , 'mobile_tel' , 'home_tel' , 'email' , 'address']
            for key in keys:
                if key in request.form:
                    params[key] = request.form[key]
            staff.edit(**params)
            return '' , 200
        except Exception:
            return '' , 500
    elif request.method == 'DELETE':
        try:
            staff.delete(staff_id)
            return '' , 200
        except Exception:
            return '' , 500
        
# TODO: Add route for add medical_staff with type doctor / pharmacist / nurse , also add in Doctor table 

@api.route('/department', methods=('GET', 'POST', 'PATCH', 'DELETE'))
def department_route():
    if request.method == 'GET':
        return jsonify(department.getDepartment())
    elif request.method == 'POST':
        try:
            params = {
                'name' : request.form['name'],
                'manager' : request.form['manager'],
                'location' : request.form['location'],
            }
            department.insertDepartment(**params)
        except HTTPException as e:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        return jsonify(request.form)
    elif request.method == 'PATCH':
        # TODO: edit department
        print(request.form)
        return jsonify(request.form)

@api.route('/patient', methods=('GET', 'POST'))
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
            patient.insertPatient(**params)
        except HTTPException as e:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        return jsonify(request.form)

@api.route('/appoint', methods=('GET', 'POST'))
def appoint_route():
    if request.method == 'GET':
        return jsonify(appoint.getAppoint())
    elif request.method == 'POST':
        appoint.insertAppoint(
            doctor_id=request.form['doctor_id'] , 
            patient_id=request.form['patient_id'] , 
            appoint_date=request.form['appoint_date']
        )
        return jsonify(request.form)