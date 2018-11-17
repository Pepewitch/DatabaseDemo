from flask import Blueprint, request, jsonify
from model import staff
from model import department
from model import patient
from dateutil import parser

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/medical_staff')
def medical_staff_route():
    medical_type = request.args.get('type')
    return jsonify(staff.getMedicalStaff(medical_type=medical_type))

@api.route('/department', methods=('GET', 'POST', 'PATCH', 'DELETE'))
def department_route():
    if request.method == 'GET':
        return jsonify(department.getDepartment())
    elif request.method == 'POST':
        try:
            if 'name' in request.form:
                if 'manager' in request.form:
                    department.insertDepartment(
                        name=request.form['name'],
                        location=request.form['location'], 
                        manager=int(request.form['manager'])
                    )
                else:
                    department.insertDepartment(
                        name=request.form['name'],
                        location=request.form['location'], 
                    )
        except Exception as e:
            print('Exception' , e)
        return jsonify(request.form)
    else:
        print(request.form)
        return jsonify(request.form)

@api.route('/patient', methods=('GET', 'POST'))
def patient_route():
    if request.method == 'GET':
        return jsonify(patient.getPatient())
    elif request.method == 'POST':
        patient.insertPatient(
            firstname=request.form['firstname'] , 
            lastname=request.form['lastname'] ,
            sex=request.form['sex'] ,
            birthdate=parser(request.form['birthdate']),
            address=request.form['address'],
            phone=request.form['phone'],
            parent_firstname=request.form['parent_firstname'],
            parent_lastname=request.form['parent_lastname'],
            parent_phone=request.form['parent_phone']
        )
        return jsonify(request.form)