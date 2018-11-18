from flask import Blueprint, request, jsonify
from model import staff
from werkzeug.exceptions import HTTPException

medical_staff_api = Blueprint('medical_staff_api', __name__ , url_prefix='/api/medical_staff')

@medical_staff_api.route('/' , methods=('GET',))
def medical_staff_route():
    try:
        params = {
            'medical_type' : request.args.get('type'),
            'staff_id' : request.args.get('id')
        }
        return jsonify(staff.getMedicalStaff(**params))
    except Exception:
        return '' , 500

@medical_staff_api.route('/<staff_id>' , methods=('GET' , 'PATCH' , 'DELETE'))
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