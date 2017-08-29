from ..cluster import cluster
from ..dbmodels import Cluster,Hosts
from flask import flash,redirect,url_for,render_template
from .. import db
from flask_login import login_required

@cluster.route('/')
@login_required
def esxi():
	jisuan('cluster1')
	jisuan('cluster2')		
	jisuan('cluster3')		
	cluster = Cluster.query.all()
	return render_template('cluster.html',cluster=cluster)
def jisuan(cluster):
	host = Hosts.query.filter_by(cluster=cluster).all()
	cluster = Cluster.query.filter_by(name=cluster).first()
	b = 0
	c = 0
	for i in host:
		if i.cpu != None:
			c = c + int(i.cpu)
		if i.ram != None:
			b = b + int(i.ram)
	cluster.used_cpus = c
	cluster.used_mem = b
	db.session.add(cluster)
	db.session.commit()	
