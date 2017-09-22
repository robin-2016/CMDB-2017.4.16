from ..main import main
from flask import render_template,request,redirect,url_for,flash,session
from ..models import InsertForm,UpdateForm,OffForm
#from ..conn import Hostservers,Selectupdate,Deldata
from flask_login import login_required
from ..dbmodels import Hosts
from .. import db

@main.route('/hosts')
@login_required
def index():
	host = Hosts.query.filter_by(closedtime=None).all()
	return render_template('data2.html',host=host)

@main.route('/insert',methods = ['GET','POST'])
@login_required
def insert():
	myform = InsertForm(request.form)
	if request.method == 'POST':
		if myform.validate_on_submit():
			print myform.data
			print type(myform.data)
			hostinsert= Hosts(body=myform.data)	
			db.session.add(hostinsert)
			db.session.commit()
			myform.status.data=None
			myform.hostname.data=None
			myform.app.data=None
			myform.ip.data=None
			myform.user.data=None
			myform.os.data=None
			myform.active.data=None
			myform.cpu.data=None
			myform.ram.data=None
			myform.disk.data=None
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
		myform.body.data = hostdata.body
	if request.method == 'POST':
        	if myform.validate_on_submit():
			hostdata.body = request.form.data
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
	myform = OffForm()
	if request.method == 'POST':
		if myform.validate_on_submit():
			delhostip=str(myform.delip.data.encode("utf-8"))
			delhost = Hosts.query.filter_by(ip=delhostip).first()
			if delhost is not None:
				db.session.delete(delhost)
				db.session.commit()
				return redirect(url_for('main.index'))
			else:
				flash('Delete Failed!')
		else:
			flash('Delete Failed!')
			return render_template('del.html',form=myform)
@main.route('/home')
@login_required
def home():
	return render_template('home.html')

@main.route('/pmhost')
@login_required
def pmhost():
	#host = Hosts.query.filter_by(htype='PM')
	host = Hosts.query.filter_by(htype='PM',closedtime=None)
	return render_template('pmhost.html',host=host)

@main.route('/vmhost')
@login_required
def vmhost():
	host = Hosts.query.filter_by(htype='VM',closedtime=None)
	return render_template('vmhost.html',host=host)

@main.route('/off',methods =['GET','POST'])
@login_required
def off():
	import time
        myform = OffForm()
        if request.method == 'POST':
                if myform.validate_on_submit():
                        offhostip=str(myform.offip.data.encode("utf-8"))
                        offhost = Hosts.query.filter_by(ip=offhostip).first()
                        if offhost is not None:
				offhost.closed = 1
				offhost.closedtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				offhost.closeduser = myform.offuser.data
				offhost.status = "off"
                                db.session.add(offhost)
                                db.session.commit()
                                return redirect(url_for('main.index'))
                        else:
                                flash('Off Failed!')
                else:
                        flash('Off Failed!')
	return render_template('off.html',form=myform)
