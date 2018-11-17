from flask import Blueprint, request, jsonify
from model import staff
from model import department
from model import patient

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
                print('name' , request.form['name'])
                print('location' , request.form['location'])
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
        # Will edit to add user in staff module
        print(request.form)
        return jsonify(request.form)