from ..manageruser import manageruser
from .. import db
from ..dbmodels import Users
from flask import flash,redirect,url_for,render_template

@manageruser.route('/main',methods = ['GET','POST'])
def managermain():
	users = Users.query.all()
	return render_template('manageruser.html',users=users)
