from flask import Blueprint
from flask import render_template,request,redirect,url_for,flash,session
from ..models import InsertForm,UpdateForm,DelForm
#from ..conn import Hostservers,Selectupdate,Deldata
from flask_login import login_required
from ..dbmodels import Hosts
from .. import db

main = Blueprint('main',__name__)

@main.route('/hosts')
@login_required
def index():
	host = Hosts.query.all()
	return render_template('data2.html',host=host)

@main.route('/insert',methods = ['GET','POST'])
@login_required
def insert():
	myform = InsertForm(request.form)
	if request.method == 'POST':
		if myform.validate_on_submit():
			hostinsert = Hosts(htype=myform.htype.data,mroom=myform.mroom.data,status=myform.status.data,hostname=myform.hostname.data,app=myform.app.data,ip=myform.ip.data,user=myform.user.data,managerip=myform.mip.data,os=myform.os.data,active=myform.active.data,location=myform.location.data,produce=myform.produce.data,warranty=myform.warranty.data,model=myform.model.data,serial=myform.serial.data,cpu=myform.cpu.data,ram=myform.ram.data,disk=myform.disk.data,storage=myform.storage.data)	
			db.session.add(hostinsert)
			db.session.commit()
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
			return render_template('insert.html',form=myform)
		else:
			flash("Insert Failed!")
			return render_template('insert.html',form=myform)
	return render_template('insert.html',form=myform)

@main.route('/ip/<ip2>',methods = ['GET','POST'])
@login_required
def update2(ip2):
	myform = UpdateForm()
	hostdata = Hosts.query.filter_by(ip=str(ip2.encode("utf-8"))).first()
	if request.method == 'GET':
		myform.htype.data=hostdata.htype
		myform.mroom.data=hostdata.mroom
		myform.status.data=hostdata.status
		myform.hostname.data=hostdata.hostname
		myform.app.data=hostdata.app
		myform.ip.data=hostdata.ip
		myform.user.data=hostdata.user
		myform.mip.data=hostdata.managerip
		myform.os.data=hostdata.os
		myform.active.data=hostdata.active
		myform.location.data=hostdata.location
		myform.produce.data=hostdata.produce
		myform.warranty.data=hostdata.warranty
		myform.model.data=hostdata.model
		myform.serial.data=hostdata.serial
		myform.cpu.data=hostdata.cpu
		myform.ram.data=hostdata.ram
		myform.disk.data=hostdata.disk
		myform.storage.data=hostdata.storage
	if request.method == 'POST':
        	if myform.validate_on_submit():
			print hostdata.htype
			hostdata.htype=request.form['htype']
			hostdata.mroom=request.form['mroom']
			hostdata.status=request.form['status']
			hostdata.hostname=request.form['hostname']
			hostdata.app=request.form['app']
			hostdata.ip=request.form['ip']
			hostdata.user=request.form['user']
			hostdata.managerip=request.form['mip']
			hostdata.os=request.form['os']
			hostdata.active=request.form['active']
			hostdata.location=request.form['location']
			hostdata.produce=request.form['produce']
			hostdata.warranty=request.form['warranty']
			hostdata.model=request.form['model']
			hostdata.serial=request.form['serial']
			hostdata.cpu=request.form['cpu']
			hostdata.ram=request.form['ram']
			hostdata.disk=request.form['disk']
			hostdata.storage=request.form['storage']
			db.session.add(hostdata)
			db.session.commit()
			return redirect(url_for('main.index'))
		else:
			flash('Update Failed!')	
			return render_template('update.html',form=myform)
	return render_template('update.html',form=myform)
#	return render_template('update.html',name=name,message=message,form=myform)
@main.route('/export')
def exportexcle():
	return redirect(url_for('main.index'))
	
@main.route('/del',methods =['GET','POST'])
@login_required
def delhost():
	myform = DelForm()
	if request.method == 'POST':
		if myform.validate_on_submit():
			delhost = Hosts.query.filter_by(ip=str(myform.delip.data.encode("utf-8"))).first()
			if delhost is not None:
				db.session.delete(delhost)
				db.session.commit()
				return redirect(url_for('main.index'))
			else:
				flash('Delete Failed!')
		else:
			flash('Delete Failed!')
			return render_template('del.html',form=myform)
	return render_template('del.html',form=myform)

