from flask import Blueprint
from flask import render_template,request,redirect,url_for,flash,session
from ..models import InsertForm,UpdateForm,DelForm,LoginForm,UseraddForm
from ..conn import Hostservers,Selectupdate,Deldata
from flask_login import login_user,login_required,current_user
from ..dbmodels import Users
from .. import db

main = Blueprint('main',__name__)

name = 'Guest'

@main.route('/',methods = ['GET','POST'])
def login():
        myform = LoginForm()
        if myform.validate_on_submit():
                username = Users.query.filter_by(name=myform.username.data).first()
		if username is not None and username.verify_password(myform.passwd.data):
			login_user(username,myform.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Username or Password is error!')		
        return render_template('login.html',name=current_user.name,form=myform)
@main.route('/useradd',methods = ['GET','POST'])
def useradd():
	myform = UseraddForm()
        if myform.validate_on_submit():
		u = Users()
		u.password_hash = myform.passwd.data
		user = Users(name=myform.username.data,passwd=u.passwd)
		db.session.add(user)
		db.session.commit()
		flash('User add Successful!')
        return render_template('useradd.html',name=current_user.name,form=myform)
	

@main.route('/hosts')
@login_required
def index():
	host = Hostservers.selectdata()	
	rows = int(str(host[1][0][0]))
	return render_template('data2.html',name=current_user.name,rows=rows,host=host[0])

@main.route('/insert',methods = ['GET','POST'])
@login_required
def insert():
	myform = InsertForm(request.form)
	if request.method == 'POST':
		if myform.validate_on_submit():
			hostinsert = Hostservers(myform.htype.data,myform.mroom.data,myform.status.data,myform.hostname.data,myform.app.data,myform.ip.data,myform.user.data,myform.mip.data,myform.os.data,myform.active.data,myform.location.data,myform.produce.data,myform.warranty.data,myform.model.data,myform.serial.data,myform.cpu.data,myform.ram.data,myform.disk.data,myform.storage.data)	
			hostinsert.insertdata()
			myform.htype.data=None
			myform.mroom.data=None
			myform.status.data=None
			myform.hostname.data=None
			myform.app.data=None
			myform.ip.data=None
			myform.user.data=None
			myform.mip.data=None
			myform.os.data=None
			myform.active.data=None
			myform.location.data=None
			myform.produce.data=None
			myform.warranty.data=None
			myform.model.data=None
			myform.serial.data=None
			myform.cpu.data=None
			myform.ram.data=None
			myform.disk.data=None
			myform.storage.data=None
			flash("Insert Successful!")
			return render_template('insert.html',name=current_user.name,form=myform)
		else:
			flash("Insert Failed!")
			return render_template('insert.html',name=current_user.name,form=myform)
	return render_template('insert.html',name=current_user.name,form=myform)

#@main.route('/update',methods = ['GET','POST'])
#def updatedb():
#	form = UpdateForm(request.form)
#	form.htype.data="PM"
#	return render_template('update.html',name=current_user.name,form=form)

@main.route('/ip/<ip>',methods = ['GET','POST'])
@login_required
def update2(ip):
	myform = UpdateForm(request.form)
	ipstring = str(ip.encode("utf-8"))
	if request.method == 'GET':
		hostupdate = Selectupdate()
		data = hostupdate.selectip(ipstring)
		myform.htype.data=data[0][1]
		myform.mroom.data=data[0][2]
		myform.status.data=data[0][3]
		myform.hostname.data=data[0][4]
		myform.app.data=data[0][5]
		myform.ip.data=data[0][6]
		myform.user.data=data[0][7]
		myform.mip.data=data[0][8]
		myform.os.data=data[0][9]
		myform.active.data=data[0][10]
		myform.location.data=data[0][11]
		myform.produce.data=data[0][12]
		myform.warranty.data=data[0][13]
		myform.model.data=data[0][14]
		myform.serial.data=data[0][15]
		myform.cpu.data=data[0][16]
		myform.ram.data=data[0][17]
		myform.disk.data=data[0][18]
		myform.storage.data=data[0][19]
	elif request.method == 'POST':
                if myform.validate_on_submit():
                        hostupdate = Hostservers(myform.htype.data,myform.mroom.data,myform.status.data,myform.hostname.data,myform.app.data,myform.ip.data,myform.user.data,myform.mip.data,myform.os.data,myform.active.data,myform.location.data,myform.produce.data,myform.warranty.data,myform.model.data,myform.serial.data,myform.cpu.data,myform.ram.data,myform.disk.data,myform.storage.data)
                        hostupdate.updatehost()
			return redirect(url_for('index'))
		else:
			flash('Update Failed!')	
			return render_template('update.html',name=current_user.name,form=myform)
	return render_template('update.html',name=current_user.name,form=myform)
#	return render_template('update.html',name=name,message=message,form=myform)
@main.route('/export')
def exportexcle():
	return redirect(url_for('index'))
	
@main.route('/del',methods =['GET','POST'])
@login_required
def delhost():
	myform = DelForm(request.form)
	if request.method == 'POST':
		if myform.validate_on_submit():
			delip = myform.delip.data
			hostdel = Deldata()
			hostdel.delhost(delip)
			return redirect(url_for('index'))
		else:
			flash('Delete Failed!')
			return render_template('del.html',name=current_user.name,form=myform)
	return render_template('del.html',name=current_user.name,form=myform)

