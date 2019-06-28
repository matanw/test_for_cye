import requests
from flask_jwt_extended import get_jwt_identity, create_access_token
from sqlalchemy import and_

from word_count_service.db.db_manager import db
from word_count_service.user_managment.user_entity import User
import requests


CAPTCHA_SECTRET_KEY="6LeOH6sUAAAAABcq4MLfwsYQIEuiHY3MtvVkv_gD"
class UserService():
    def init_users(self):
        if not User.query.all():
            db.session.add(User(username='user1',password='pass1'))
            db.session.add(User(username='user2',password='pass2'))
            db.session.commit()

    def get_by_username_and_password(self,username,password):
        return  User.query.filter(and_(User.username == username,User.password==password)).one_or_none()

    def get_currect_user_id(self):
        return get_jwt_identity()

    def get_access_token(self,user):
        return create_access_token(user.username)

    def verify_captcha(self,captcha):
        google_response= requests.post("https://www.google.com/recaptcha/api/siteverify", data={"secret": CAPTCHA_SECTRET_KEY,
                                                                                     "response": captcha}).json()
        print("Captcha response:",google_response)#todo: add log
        if not google_response["success"]:
            raise  Exception()#todo: api error



user_service=UserService()