from flask import Blueprint , request , jsonify
from model import staff

api = Blueprint('api' , __name__ , url_prefix='/api')

@api.route('/medical_staff' , methods=('GET' , 'POST'))
def medical_staff():
    print(request)
    if request.method == 'GET':
        return jsonify(staff.getMedicalStaff())
    else:
        # Will edit to add user in staff module
        print(request.form)
        return jsonify(request.form)
