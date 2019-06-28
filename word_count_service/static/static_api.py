from flask import request
from flask_restplus import Namespace, Resource, fields

from word_count_service.app import app
from word_count_service.exception_handling import exception_wrapper

static_ns = Namespace('static', description='static page')

@static_ns.route('/')
class StaticApi(Resource):

    @exception_wrapper
    def get(self):
        return app.send_static_file('index.html')

