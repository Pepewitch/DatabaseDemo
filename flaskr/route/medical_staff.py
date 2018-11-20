from flask import Blueprint, request, jsonify
from model import staff
from werkzeug.exceptions import HTTPException
from dateutil import parser

medical_staff_api = Blueprint('medical_staff_api', __name__ , url_prefix='/api')

@medical_staff_api.route('/medical_staff' , methods=('GET',))
def medical_staff_route():
    try:
        params = {
            'medical_type' : request.args.get('type'),
            'staff_id' : request.args.get('id')
        }
        return jsonify(staff.getMedicalStaff(**params))
    except Exception:
        return '' , 500

@medical_staff_api.route('/medical_staff/<staff_id>' , methods=('GET' , 'PATCH' , 'DELETE'))
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
            keys = ['sex' , 'salary' , 'mobile_tel' , 'home_tel' , 'email' , 'address' , 'firstname' , 'lastname']
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
        
@medical_staff_api.route('/medical_staff/doctor' , methods=('GET' , 'POST'))
def medical_staff_doctor_route():
    print(request.form)
    if request.method == 'GET':
        try:
            params = {
                'medical_type' : 'Doctor',
                'staff_id' : None
            }
            return jsonify(staff.getMedicalStaff(**params))
        except Exception:
            return '' , 500
    elif request.method == 'POST':
        try:
            params = {
                'sex': request.form['sex'] ,
                'salary': request.form['salary'], 
                'mobile_tel': request.form['mobile_tel'], 
                'home_tel': request.form['home_tel'], 
                'email': request.form['email'], 
                'address': request.form['address'],
                'doctor_type': request.form['doctor_type'],
                'birthdate': parser.parse(request.form['birthdate']).strftime('%Y-%m-%d'),
                'firstname' : request.form['firstname'] ,
                'lastname' : request.form['lastname']
            }
            staff.insertDoctor(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            print(e)
            return '' , 500

@medical_staff_api.route('/medical_staff/nurse' , methods=('GET' , 'POST'))
def medical_staff_nurse_route():
    if request.method == 'GET':
        try:
            params = {
                'medical_type' : 'Nurse',
                'staff_id' : None
            }
            return jsonify(staff.getMedicalStaff(**params))
        except Exception:
            return '' , 500
    elif request.method == 'POST':
        try:
            params = {
                'sex': request.form['sex'] ,
                'salary': request.form['salary'], 
                'mobile_tel': request.form['mobile_tel'], 
                'home_tel': request.form['home_tel'], 
                'email': request.form['email'], 
                'address': request.form['address'],
                'nurse_type': request.form['nurse_type'],
                'birthdate': parser.parse(request.form['birthdate']).strftime('%Y-%m-%d'),
                'nurse_type': request.form['nurse_type'],
                'firstname' : request.form['firstname'] ,
                'lastname' : request.form['lastname']
            }
            staff.insertNurse(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            print(e)
            return '' , 500

@medical_staff_api.route('/medical_staff/pharmacist' , methods=('GET' , 'POST'))
def medical_staff_pharmacist_route():
    if request.method == 'GET':
        try:
            params = {
                'medical_type' : 'Pharmacist',
                'staff_id' : None
            }
            return jsonify(staff.getMedicalStaff(**params))
        except Exception:
            return '' , 500
    elif request.method == 'POST':
        try:
            params = {
                'sex': request.form['sex'] ,
                'salary': request.form['salary'], 
                'mobile_tel': request.form['mobile_tel'], 
                'home_tel': request.form['home_tel'], 
                'email': request.form['email'], 
                'address': request.form['address'],
                'pharmacist_type': request.form['pharmacist_type'],
                'birthdate': parser.parse(request.form['birthdate']).strftime('%Y-%m-%d'),
                'pharmacist_type': request.form['pharmacist_type'],
                'firstname' : request.form['firstname'] ,
                'lastname' : request.form['lastname']
            }
            staff.insertPharmacist(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            print(e)
            return '' , 500