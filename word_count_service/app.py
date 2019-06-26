from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)

def init_app():
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///example3.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    #todo: refactor, split this logic

    from word_count_service.db.db_manager import db
    db.init_app(app) #todo: why need db.app=app ? maybe fix this bug in flask
    db.app=app

    # todo: protect from auto deltion
    from word_count_service.word_stats.word_stats_entities import WordStatsResult, WordStats

    db.create_all()
    from word_count_service.word_stats.word_stats_api import ns
    api.add_namespace(ns)
    app.run(debug=True)


if __name__ == '__main__':
    init_app()