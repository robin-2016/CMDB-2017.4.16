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
	status = db.Column(db.String(8))
	hostname = db.Column(db.String(80))
	app = db.Column(db.String(100))
	ip = db.Column(db.String(15))
	user = db.Column(db.String(50))
	os = db.Column(db.String(50))
	active = db.Column(db.String(4))
	cpu = db.Column(db.Integer)
	ram = db.Column(db.Integer)
	disk = db.Column(db.String(20))
	group_id = db.Column(db.Integer,db.ForeignKey('devegroup.nu'))
	cluster_id = db.Column(db.Integer,db.ForeignKey('cluster.nu'))
	project_id = db.Column(db.Integer,db.ForeignKey('project.nu'))
	closedtime = db.Column(db.DateTime)
	closeduser = db.Column(db.String(40))

class Pm(db.Model):
        __tablename__= 'pm'
        nu = db.Column(db.Integer,primary_key=True)
        hostname = db.Column(db.String(80))
	cputype = db.Column(db.String(50))
	cputoal = db.Column(db.Integer)
	cpunu = db.Column(db.Integer)
	cputh = db.Column(db.Integer)
	memtoal = db.Column(db.Integer)
	memnu = db.Column(db.Integer)
	memsize = db.Column(db.Integer)
        managerip = db.Column(db.String(50))
        location = db.Column(db.String(20))
        produce = db.Column(db.String(20))
        warranty = db.Column(db.String(20))
        model = db.Column(db.String(50))
        serial = db.Column(db.String(100))
        disk = db.Column(db.String(20))

class Cluster(db.Model):
	__tablename__= 'cluster'
	nu = db.Column(db.Integer,primary_key=True)
	cname = db.relationship('Hosts',backref='cluster')
	cpus = db.Column(db.Integer)
	mem = db.Column(db.Integer)
	used_cpus = db.Column(db.Integer)
	used_mem = db.Column(db.Integer)

class devegroup(db.Model):
	__tablename__= 'devegroup'
	nu = db.Column(db.Integer,primary_key=True)
	gname = db.relationship('Hosts',backref='gname')

class Project(db.Model):
	__tablename__= 'project'
	nu = db.Column(db.Integer,primary_key=True)
	pname = db.relationship('Hosts',backref='pname')
#class Group(db.Model):
#	__tablename__= 'group'
#	nu = db.Column(db.Integer,primary_key=True)
#	pname = db.Column(db.String(60))
