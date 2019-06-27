from word_count_service.db.db_manager import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String(255),unique=True)
    password =db.Column(db.String(255),unique=False)