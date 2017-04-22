from app import db,login_manager
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class Users(UserMixin,db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer,primary_key=True)
        name = db.Column(db.String(50),unique=True)
        passwd = db.Column(db.String(100))
        role = db.Column(db.String(20))

        @property
        def password_hash(self):
                raise AttributeError('Password is not a readable attribute!')
        @password_hash.setter
        def password_hash(self,password):
                self.passwd = generate_password_hash(password)
        def verify_password(self,password):
                return check_password_hash(self.passwd,password)
	@login_manager.user_loader
	def load_user(user_id):
		return Users.query.get(int(user_id))
