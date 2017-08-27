from ..offhost import offhost
from ..dbmodels import Hosts
from flask import flash,redirect,url_for,render_template
from .. import db

@offhost.route('/')
def offhost():
	offhost = Hosts.query.filter_by(closed='1').all()
	return render_template('offhost.html',offhost=offhost)
