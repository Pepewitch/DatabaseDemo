#!/usr/bin/env python3

from cheroot.wsgi import Server, PathInfoDispatcher
from flask import Flask , send_file
from model import staff
from os.path import join

app = Flask(__name__)

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
