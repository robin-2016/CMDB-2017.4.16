from ..mhosts import mhosts
from random import Random
from ..models import Hostpasswd
from flask import flash,redirect,url_for,render_template,request
import paramiko

def random_str(length=8):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!#^%'
	for i in range(length):
		str+=chars[Random().randint(0,(len(chars)-1))]
	return str

@mhosts.route("/mpasswd",methods= ['GET','POST'])
def mpasswd():
	myform = Hostpasswd()
	if request.method == 'POST':
                if myform.validate_on_submit():
			hip = myform.hip.data
			hpd =  myform.hpd.data
			hostpd = random_str(12) + str(hip)[-2:]
			try:
				ssh = paramiko.SSHClient()
				#ssh.load_system_host_keys()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(hostname=str(hip),username='root',password=str(hpd))
				stdin,stdout,stderr = ssh.exec_command('echo %s | passwd root --stdin' %hostpd)
				ssh.close()
				something = open("something",'a')
				somewrite = [hip,"  ",hostpd+'\n']
				something.writelines(somewrite)
				something.close()
				flash("Change password successful!"+"       "+hip+" :  "+hostpd)
			except Exception,e:
				flash(e)
	return render_template('mpasswd.html',form=myform)	

