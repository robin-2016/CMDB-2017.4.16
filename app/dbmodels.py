from app import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class Users(UserMixin,db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer,primary_key=True)
        name = db.Column(db.String(50),unique=True)
        password_hash = db.Column(db.String(100))
        role = db.Column(db.String(20))

        @property
        def password(self):
                raise AttributeError('Password is not a readable attribute!')
        @password.setter
        def password(self,password):
                self.password_hash = generate_password_hash(password)
        def check_password_hash(self,password):
                return check_password_hash(self.passowrd_hash,password)
