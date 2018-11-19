from flask import Blueprint, request, jsonify
from model import department

department_api = Blueprint('department_api', __name__ , url_prefix='/api')

@department_api.route('/department', methods=('GET', 'POST', 'PATCH', 'DELETE'))
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
            return '' , 200
        except HTTPException as e:
            return jsonify({'message' : 'Arguments are invalid'}) , 400
        except Exception:
            return '' , 500
    elif request.method == 'PATCH':
        # TODO: edit department
        print(request.form)
        return jsonify(request.form)