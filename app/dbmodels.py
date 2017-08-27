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

class Hosts(db.Model):
	__tablename__= 'host'
	nu = db.Column(db.Integer,primary_key=True)
	htype = db.Column(db.String(10))
	mroom = db.Column(db.String(6))
	status = db.Column(db.String(8))
	hostname = db.Column(db.String(80))
	app = db.Column(db.String(100))
	ip = db.Column(db.String(15))
	user = db.Column(db.String(50))
	managerip = db.Column(db.String(50))
	os = db.Column(db.String(50))
	active = db.Column(db.String(4))
	location = db.Column(db.String(20))
	produce = db.Column(db.String(20))
	warranty = db.Column(db.String(20))
	model = db.Column(db.String(50))
	serial = db.Column(db.String(100))
	cpu = db.Column(db.Integer)
	ram = db.Column(db.Integer)
	disk = db.Column(db.String(20))
	storage = db.Column(db.String(20))
	cluster = db.Column(db.String(20))
	closed = db.Column(db.String(10))
	closedtime = db.Column(db.String(60))
	closeduser = db.Column(db.String(40))

#class Delhosts(Hosts):
#	__tablename__= 'delhost'
#	__table_args__ = {"useexiting": True}
#	nu = db.Column(db.Integer,primary_key=True)
#	htype = db.Column(db.String(10))
#	mroom = db.Column(db.String(6))
#	status = db.Column(db.String(8))
#	hostname = db.Column(db.String(80))
#	app = db.Column(db.String(100))
#	ip = db.Column(db.String(15),unique=True,index=True)
#	user = db.Column(db.String(50))
#	managerip = db.Column(db.String(50))
#	os = db.Column(db.String(50))
#	active = db.Column(db.String(4))
#	location = db.Column(db.String(20))
#	produce = db.Column(db.String(20))
#	warranty = db.Column(db.String(20))
#	model = db.Column(db.String(50))
#	serial = db.Column(db.String(100))
#	cpu = db.Column(db.Integer)
#	ram = db.Column(db.Integer)
#	disk = db.Column(db.String(20))
#	storage = db.Column(db.String(20))
#	cluster = db.Column(db.String(20))

class Cluster(db.Model):
	__tablename__= 'cluster'
	nu = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(20))
	cpus = db.Column(db.Integer)
	mem = db.Column(db.Integer)
	used_cpus = db.Column(db.Integer)
	used_mem = db.Column(db.Integer)
		
