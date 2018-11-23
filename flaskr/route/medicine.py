from flask import Blueprint, request, jsonify
from model import medicine
from werkzeug.exceptions import HTTPException
from dateutil import parser

medicine_api = Blueprint('medicine_api', __name__ , url_prefix='/api')

@medicine_api.route('/medicine' , methods=('GET','POST'))
def medicine_route():
    print(request.args)
    if request.method == 'GET': #done
        try:
            params = {
                'medicine_id' : request.args.get('id')
            }
            print(params)
            return jsonify(medicine.getMedicine(**params))
        except Exception:
            return '' , 500
    elif request.method == 'POST': #done
        print(request)
        try:
            params = {
                'name': request.form['name'],
                'quantity': request.form['quantity'], 
                'exp_date': request.form['exp_date']
            }
            print(params)
            medicine.insertMedicine(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            print(e)
            return '' , 500

        

@medicine_api.route('/medicine/<medicine_id>' , methods=('GET' , 'PATCH' , 'DELETE'))
def medicine_id_route(medicine_id):
    if request.method == 'GET': #done
        try:
            params = {
                'medicine_id' : medicine_id
            }
            return jsonify(medicine.getMedicine(**params))
        except Exception:
            return '' , 500
    # elif request.method == 'PATCH': 
    #     try:
    #         params = { 'medicine_id' : medicine_id }
    #         keys = ['name' , 'quantity' , 'exp_date']
    #         for key in keys:
    #             if key in request.form:
    #                 params[key] = request.form[key]
    #         medicine.edit(**params)
    #         return '' , 200
    #     except Exception:
    #         return '' , 500
    elif request.method == 'DELETE': #done
        try: 
            medicine.delete(medicine_id)
            return '' , 200
        except Exception:
            return '' , 500
        
@medicine_api.route('/medicine/refill' , methods=('POST',))  #done
def medicine_refill_route():
    print(request.form)
    if request.method == 'POST':
        try:
            params = {
                'medicine_id': request.form['medicine_id'] ,
                'pharmacist_id': request.form['pharmacist_id'], 
                'quantity': request.form['quantity']
            }
            medicine.refillMedicine(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            print(e)
            return '' , 500

@medicine_api.route('/medicine/perscribe' , methods=('POST','GET'))
def medicine_perscribe_route():
    print(request.args)
    if request.method == 'GET' : #done
        try:
            params = {
                'medicine_id' : request.args.get('medicine_id'),
                'doctor_id' : request.args.get('doctor_id'),
                'patient_id' : request.args.get('patient_id')
            }
            print(params)
            return jsonify(medicine.getPerscribe(**params))
        except Exception:
            return '' , 500
    elif request.method == 'POST': #done
        try:
            params = {
                'medicine_id': request.form['medicine_id'] ,
                'patient_id': request.form['patient_id'], 
                'doctor_id': request.form['doctor_id'], 
                'quantity' : request.form['quantity']
            }
            medicine.perscribeMedicine(**params)
            return '' , 200
        except HTTPException:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception as e:
            print(e)
            return '' , 500

