class Config:
	SECRET_KEY = 'test321'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql://root:&UJM7ujm@10.0.2.10:3306/CMDB"
class ProductionConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql://root:'&UJM7ujm'@10.0.2.10:3306/CMDB"
config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig	
}
