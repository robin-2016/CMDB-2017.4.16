#/bin/python
#-*-coding=utf-8-*-

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'

def creat_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
#	print config[config_name]
	config[config_name].init_app(app)
	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .user import user as user_blueprint
	app.register_blueprint(user_blueprint)
	from .manageruser import manageruser as manageruser_blueprint
	app.register_blueprint(manaageruser_blueprint)
	return app
