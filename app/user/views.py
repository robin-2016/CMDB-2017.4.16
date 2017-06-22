from ..user import user
from flask_login import login_user,logout_user,login_required,current_user
from flask import flash,redirect,url_for,render_template,session
from ..models import LoginForm,UseraddForm,ChangepwForm
from .. import db
from ..dbmodels import Users

@user.route('/',methods = ['GET','POST'])
def login():
        myform = LoginForm()
        if myform.validate_on_submit():
                username = Users.query.filter_by(name=myform.username.data).first()
                if username is not None and username.verify_password(myform.passwd.data):
                        login_user(username,myform.remember_me.data)
                        session['role'] = username.role
                        print session.get('role')
                        return redirect(url_for('main.index'))
                flash('Username or Password is error!')
        return render_template('login.html',form=myform)

@user.route('/logout')
@login_required
def logout():
        logout_user()
        flash('Logout Successful!')
        return redirect(url_for('user.login'))

@user.route('/useradd',methods = ['GET','POST'])
#######@login_required
def useradd():
        myform = UseraddForm()
        if myform.validate_on_submit():
                u = Users()
                u.password_hash = myform.passwd.data
#                user = Users(name=myform.username.data,passwd=u.passwd)
                u.name = myform.username.data
                db.session.add(u)
                db.session.commit()
                flash('User add Successful!')
                myform.username.data = None
        return render_template('useradd.html',form=myform)

@user.route('/userchange',methods=['GET','POST'])
@login_required
def userchange():
        myform = ChangepwForm()
        if myform.validate_on_submit():
                user = Users.query.filter_by(name=current_user.name).first()
                if user is not None and user.verify_password(myform.passwdold.data):
                        user.password_hash = myform.passwd.data
                        db.session.add(user)
                        db.session.commit()
                        flash('Password change Successfull!')
                        return redirect(url_for('main.index'))
                else:
                        flash('Change Fialed!')
                        return render_template('changepw.html',form=myform)
        return render_template('changepw.html',form=myform)
