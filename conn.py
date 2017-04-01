import MySQLdb

def get_conn():
	conn = MySQLdb.connect(host = "10.0.2.10",user = "root",passwd = "&UJM7ujm",db = "CMDB",charset="utf8")
	return conn
class Hosts(object):
	def __init__(self,htype,mroom,status,hostname,app,ip,user,mip,os,active,location,produce,warranty,model,serial,cpu,ram,disk,storage):
		self.htype = htype
                self.mroom = mroom
                self.status = status
                self.hostname = hostname
                self.app = app
                self.ip = ip
                self.user = user
                self.mip = mip
                self.os = os
                self.active = active
                self.location = location
                self.produce = produce
                self.warranty = warranty
                self.model = model
                self.serial = serial
                self.cpu = cpu
                self.ram = ram
                self.disk = disk
                self.storage = storage
	def insertdata(self):
		dbconn = get_conn()
		cursor = dbconn.cursor()
		sql = "INSERT INTO host (type,mroom,status,hostname,app,ip,user,managerip,os,active,location,produce,warranty,model,serial,cpu,ram,disk,storage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(sql,(self.htype,self.mroom,self.status,self.hostname,self.app,self.ip,self.user,self.mip,self.os,self.active,self.location,self.produce,self.warranty,self.model,self.serial,self.cpu,self.ram,self.disk,self.storage))
		dbconn.commit()
		cursor.close()
		dbconn.close()
	@staticmethod
	def selectdata():
		data = []
		dbconn = get_conn()
		cursor = dbconn.cursor()
		sql = "select * from host"
		sql2 = "select count(nu) from host"
		cursor.execute(sql)
		data1 = cursor.fetchall()
		cursor.execute(sql2)
		data2 = cursor.fetchall()
		dbconn.commit()
		cursor.close()
		dbconn.close()
		data.append(data1)
		data.append(data2)
		return data
class Selectdata(object):
	def selectip(ip):
		dbconn = get_conn()
		cursor = dbconn.cursor()
		sql = "select * from host where ip = '%s'"
		cursor.execute(sql,ip)
		data = cursor.fetchall()
		dbconn.commit()
		cursor.close()
		dbconn.close()
		return data
