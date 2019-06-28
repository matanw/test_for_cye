from flask import request
from flask_restplus import Namespace, Resource, fields

from word_count_service.exception_handling import exception_wrapper, ApiException
from word_count_service.user_managment.user_service import user_service
from word_count_service.word_stats.word_stats_service import word_count_service
from word_count_service.word_stats.word_stats_transformer import words_stats_transformer

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity)
login_ns = Namespace('login', description='login')

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity)
login_request= login_ns.model('login', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The password'),
    'captcha': fields.String(required=True, description='captcha')
})

login_result= login_ns.model('login', {
    'access_token': fields.String(required=True, description='The access_ token')
})


@login_ns.route('/')
class LoginApi(Resource):
    @exception_wrapper
    @login_ns.doc('fetch words frequencies by url')
    @login_ns.expect(login_request)
    @login_ns.marshal_with(login_result)
    def post(self):
        payload=request.json
        user_service.verify_captcha(payload["captcha"])
        user=user_service.get_by_username_and_password(payload["username"], payload["password"])
        if user is None:
            raise  ApiException("Wrong credentials",401)
        access_token=user_service.get_access_token(user)
        return {"access_token":access_token}
