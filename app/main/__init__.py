from flask import Blueprint
from flask import render_template,request,redirect,url_for,flash,session
from ..models import InsertForm,UpdateForm,DelForm
from ..conn import Hostservers,Selectupdate,Deldata
from flask_login import login_required,current_user
from ..dbmodels import Hosts
from .. import db

main = Blueprint('main',__name__)

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

@main.route('/ip/<ip2>',methods = ['GET','POST'])
@login_required
def update2(ip2):
	myform = UpdateForm(request.form)
	if request.method == 'GET':
		hostdata = Hosts.query.filter_by(ip=str(ip2.encode("utf-8"))).all()
		for hdata in hostdata:
			myform.htype.data=hdata.htype
			myform.mroom.data=hdata.mroom
			myform.status.data=hdata.status
			myform.hostname.data=hdata.hostname
			myform.app.data=hdata.app
			myform.ip.data=hdata.ip
			myform.user.data=hdata.user
			myform.mip.data=hdata.managerip
			myform.os.data=hdata.os
			myform.active.data=hdata.active
			myform.location.data=hdata.location
			myform.produce.data=hdata.produce
			myform.warranty.data=hdata.warranty
			myform.model.data=hdata.model
			myform.serial.data=hdata.serial
			myform.cpu.data=hdata.cpu
			myform.ram.data=hdata.ram
			myform.disk.data=hdata.disk
			myform.storage.data=hdata.storage
	elif request.method == 'POST':
                if myform.validate_on_submit():
			hostupdate = Hosts(htype=myform.htype.data,mroom=myform.mroom.data,status=myform.status.data,hostname=myform.hostname.data,app=myform.app.data,ip=myform.ip.data,user=myform.user.data,managerip=myform.mip.data,os=myform.os.data,active=myform.active.data,location=myform.location.data,produce=myform.produce.data,warranty=myform.warranty.data,model=myform.model.data,serial=myform.serial.data,cpu=myform.cpu.data,ram=myform.ram.data,disk=myform.disk.data,storage=myform.storage.data)	
			db.session.update(hostupdate)
			db.session.commit()
			return redirect(url_for('main.index'))
		else:
			flash('Update Failed!')	
			return render_template('update.html',name=current_user.name,form=myform)
	return render_template('update.html',name=current_user.name,form=myform)
#	return render_template('update.html',name=name,message=message,form=myform)
@main.route('/export')
def exportexcle():
	return redirect(url_for('main.index'))
	
@main.route('/del',methods =['GET','POST'])
@login_required
def delhost():
	myform = DelForm(request.form)
	if request.method == 'POST':
		if myform.validate_on_submit():
			delhost = Hosts(ip=myform.delip.data)
			db.session.delete(delhost)
			db.session.commit()
			return redirect(url_for('main.index'))
		else:
			flash('Delete Failed!')
			return render_template('del.html',name=current_user.name,form=myform)
	return render_template('del.html',name=current_user.name,form=myform)

