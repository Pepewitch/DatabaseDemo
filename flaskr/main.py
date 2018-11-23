#!/usr/bin/env python3

from cheroot.wsgi import Server, PathInfoDispatcher
from flask import Flask, send_file
from model import staff
from os.path import join
from flask_cors import CORS
from route.medical_staff import medical_staff_api
from route.appoint import appoint_api
from route.patient import patient_api
from route.department import department_api
from route.medicine import medicine_api

app = Flask(__name__)
CORS(app)
app.register_blueprint(medical_staff_api)
app.register_blueprint(appoint_api)
app.register_blueprint(patient_api)
app.register_blueprint(department_api)
app.register_blueprint(medicine_api)

@app.route("/")
def index():
    return send_file(join('..','view','index.html'))

@app.route("/test")
def test():
    return str(staff.test())

if __name__ == '__main__':
	d = PathInfoDispatcher({'/': app})
	server = Server(('0.0.0.0', 8080), d)
	try:
		server.start()
	except KeyboardInterrupt:
		server.stop()
