#/bin/python
#-*-coding=utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask_wtf import FlaskForm
from wtforms import TextField,validators,SubmitField,StringField,PasswordField,BooleanField,SelectField,IntegerField
from wtforms.validators import Required,Length,Regexp,EqualTo
from .dbmodels import Users

class FormClass(FlaskForm):
        htype = SelectField("*类型",choices=[('VM','VM'),('PM','PM')])
        status = SelectField("*状态",choices=[('使用中','使用中'),('已关机','已关机'),('已删除','已删除')])
        hostname = TextField("*主机名",[validators.Required()])
        app = TextField("*应用名称",[validators.Required()])
        ip = TextField("*内网IP",[validators.IPAddress()])
        user = TextField("*应用负责人",[validators.Required()])
        os = TextField("*操作系统",[validators.Required()])
        active = TextField("*激活",[validators.Required()])
        cpu = IntegerField("*CPU",[validators.Required()])
        ram = IntegerField("*内存",[validators.Required()])
	cluster = SelectField("集群",choices=[('cluster1','cluster1'),('cluster2','cluster2'),('cluster3','cluster3'),('物理机','物理机')]) 
        disk = TextField("硬盘Raid")
	gname = SelectField("开发分组",choices=[('开发一组','开发一组'),('开发二组','开发二组'),('联动北京','联动北京')])
	pname = SelectField("项目分组",choices=[('钱吧','钱吧'),('CRM','CRM'),('联动汽车','联动汽车'),('抵质押','抵质押')])
class InsertForm(FormClass):
        submit = SubmitField("新增")
class UpdateForm(FormClass):
        submit = SubmitField("更新")

class OffForm(FlaskForm):
	offip = TextField("输入要下架主机的IP",[validators.IPAddress()])
	offuser = TextField("下架通知者",[validators.Required()])
	submit = SubmitField("下架")

class LoginForm(FlaskForm):
	username = StringField("用户名：",[validators.Required()])
	passwd = PasswordField("密码：",[validators.Required()])
	remember_me = BooleanField("记住我")
	submit = SubmitField("登录")

class UseraddForm(FlaskForm):
	username = StringField("用户名：",validators=[Required(),Length(1,100),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'只能使用字母、数字、下划线和点号！')])
	passwd = PasswordField("密码：",validators=[Required(),EqualTo('passwd2',message='两次密码不相同！')])
	passwd2 = PasswordField("确认密码：",validators=[Required()])
	submit = SubmitField('新增用户')

	def validate_username(self,field):
		if Users.query.filter_by(name=field.data).first():
			raise ValidationError('用户名已经存在！')

class ChangepwForm(FlaskForm):
	passwdold = PasswordField("旧密码：",[validators.Required()])
	passwd = PasswordField("新密码：",validators=[Required(),EqualTo('passwd2',message='两次密码不相同！')])
	passwd2 = PasswordField("确认密码：",validators=[Required()])
	submit = SubmitField('更改密码')

class Hostpasswd(FlaskForm):
	hip = StringField("主机IP：",[validators.Required()])
	hpd = PasswordField("登录密码：",[validators.Required()])
	submit = SubmitField('更改密码')
