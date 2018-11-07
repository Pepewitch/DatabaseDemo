#!/usr/bin/env python3

from cheroot.wsgi import Server, PathInfoDispatcher
from flask import Flask
import pymysql

from model import staff

app = Flask(__name__)

@app.route("/")
def handle_():
    return str(staff.test())

if __name__ == '__main__':
	d = PathInfoDispatcher({'/': app})
	server = Server(('0.0.0.0', 8080), d)
	try:
		server.start()
	except KeyboardInterrupt:
		server.stop()
