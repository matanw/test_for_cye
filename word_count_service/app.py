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
    from word_count_service.user_managment.user_entity import User
    db.create_all()
    from word_count_service.user_managment.user_service import user_service
    user_service.init_users()

    from flask_jwt_extended import JWTManager
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)

    from word_count_service.word_stats.word_stats_api import word_stats_ns
    api.add_namespace(word_stats_ns)
    from word_count_service.user_managment.login_api import login_ns
    api.add_namespace(login_ns)
    from word_count_service.static.static_api import static_ns
    api.add_namespace(static_ns)

    app.run(debug=True)


if __name__ == '__main__':
    init_app()