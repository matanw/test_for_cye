from flask import Flask
from flask_restplus import Resource, Api

from word_count_service.word_count.word_count_api import ns

app = Flask(__name__)
api = Api(app)

api.add_namespace(ns)


if __name__ == '__main__':
    app.run(debug=True)