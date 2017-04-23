from flask import Blueprint
from flask_login import login_user,logout_user,login_required,current_user
from flask import flash,redirect,url_for,render_template,request
from ..models import LoginForm,UseraddForm
from .. import db
from ..dbmodels import Users

user = Blueprint('user',__name__)

name = 'Guest'

@user.route('/',methods = ['GET','POST'])
def login():
        myform = LoginForm()
        if myform.validate_on_submit():
                username = Users.query.filter_by(name=myform.username.data).first()
                if username is not None and username.verify_password(myform.passwd.data):
                        login_user(username,myform.remember_me.data)
                        return redirect(request.args.get('next') or url_for('main.index'))
                flash('Username or Password is error!')
        return render_template('login.html',name=name,form=myform)

@user.route('/logout')
@login_required
def logout():
        logout_user()
        flash('Logout Successful!')
        return redirect(url_for('user.login'))

@user.route('/useradd',methods = ['GET','POST'])
@login_required
def useradd():
        myform = UseraddForm()
        if myform.validate_on_submit():
                u = Users()
                u.password_hash = myform.passwd.data
                user = Users(name=myform.username.data,passwd=u.passwd)
                db.session.add(user)
                db.session.commit()
                flash('User add Successful!')
                myform.username.data = None
        return render_template('useradd.html',name=current_user.name,form=myform)
