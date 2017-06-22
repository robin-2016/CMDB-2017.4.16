import os
from flask_script import Manager,Server
from app import creat_app,db


app = creat_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("runserver",Server(host="192.168.29.129"))

if __name__ == '__main__':
	manager.run()
