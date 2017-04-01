#/bin/python
#-*-coding=utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from conn import Hosts
from wtforms import TextField,validators,SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'test321'

name = "xuhongbin"

class FormClass(FlaskForm):
	htype = TextField("type",[validators.Required()])
	mroom = TextField("mroom",[validators.Required()])
	status = TextField("status",[validators.Required()])
	hostname = TextField("hostname",[validators.Required()])
	app = TextField("app",[validators.Required()])
#	ip = TextField("ip",[validators.Required()])
	ip = TextField("ip",[validators.IPAddress()])
	user = TextField("user",[validators.Required()])
	mip = TextField("mip",[validators.Required()])
	os = TextField("os",[validators.Required()])
	active = TextField("active",[validators.Required()])
	location = TextField("location",[validators.Required()])
	produce = TextField("produce",[validators.Required()])
	warranty = TextField("warranty",[validators.Required()])
	model = TextField("model",[validators.Required()])
	serial = TextField("serial",[validators.Required()])
	cpu = TextField("cpu",[validators.Required()])
	ram = TextField("ram",[validators.Required()])
	disk = TextField("disk",[validators.Required()])
	storage = TextField("storage",[validators.Required()])
class InsertForm(FormClass):
	submit = SubmitField("新增")
class UpdateForm(FormClass):
	submit = SubmitField("更新")
@app.route('/')
def hello():
	host = Hosts.selectdata()	
	rows = int(str(host[1][0][0]))
	return render_template('data2.html',name=name,rows=rows,host=host[0])

@app.route('/insert',methods = ['GET','POST'])
def insert():
	myform = InsertForm(request.form)
	message = ""
	if request.method == 'POST':
		if myform.validate_on_submit():
			hostdata = Hosts(myform.htype.data,myform.mroom.data,myform.status.data,myform.hostname.data,myform.app.data,myform.ip.data,myform.user.data,myform.mip.data,myform.os.data,myform.active.data,myform.location.data,myform.produce.data,myform.warranty.data,myform.model.data,myform.serial.data,myform.cpu.data,myform.ram.data,myform.disk.data,myform.storage.data)	
			hostdata.insertdata()
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
			message = "Insert Successful!"
			return render_template('insert.html',name=name,message=message,form=myform)
		else:
			message = "Insert Failed!"
			return render_template('insert.html',name=name,message=message,form=myform)
	return render_template('insert.html',name=name,message=message,form=myform)

@app.route('/update',methods = ['GET','POST'])
def updatedb():
	message = ""
	form = UpdateForm(request.form)
	form.htype.data="PM"
	form.mroom.data="网信"
	return render_template('update.html',name=name,message=message,form=form)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
