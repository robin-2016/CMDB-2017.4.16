#/bin/python
#-*-coding=utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask_wtf import FlaskForm
from wtforms import TextField,validators,SubmitField,StringField,PasswordField,BooleanField
from wtforms.validators import Required,Length,Regexp,EqualTo

class FormClass(FlaskForm):
        htype = TextField("*类型",[validators.Required()])
        mroom = TextField("*机房",[validators.Required()])
        status = TextField("*状态",[validators.Required()])
        hostname = TextField("*主机名",[validators.Required()])
        app = TextField("*应用名称",[validators.Required()])
#       ip = TextField("ip",[validators.Required()])
        ip = TextField("*内网IP",[validators.Required()])
        user = TextField("*应用负责人",[validators.Required()])
        mip = TextField("管理IP")
        os = TextField("*操作系统",[validators.Required()])
        active = TextField("*激活",[validators.Required()])
        location = TextField("机架位置")
        produce = TextField("生产商")
        warranty = TextField("保修日期")
        model = TextField("设备型号")
        serial = TextField("序列号")
        cpu = TextField("*CPU",[validators.Required()])
        ram = TextField("*内存",[validators.Required()])
        disk = TextField("*硬盘Raid",[validators.Required()])
        storage = TextField("外连存储")
class InsertForm(FormClass):
        submit = SubmitField("新增")
class UpdateForm(FormClass):
        submit = SubmitField("更新")

class DelForm(FlaskForm):
	delip = TextField("输入要删除的IP",[validators.IPAddress()])
	submit = SubmitField("删除")

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
