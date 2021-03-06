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
	app.register_blueprint(manageruser_blueprint,url_prefix='/manageruser')
	from .mhosts import mhosts as mhosts_blueprint
	app.register_blueprint(mhosts_blueprint,url_prefix='/mhosts')
	from .cluster import cluster as cluster_blueprint
	app.register_blueprint(cluster_blueprint,url_prefix='/cluster')
	from .offhost import offhost as offhost_blueprint
	app.register_blueprint(offhost_blueprint,url_prefix='/offhost')
	return app
