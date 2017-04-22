import MySQLdb

def get_conn():
	conn = MySQLdb.connect(host = "192.168.192.15",user = "root",passwd = "&UJM7ujm",db = "CMDB",charset="utf8")
	return conn
class Hostservers(object):
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
	def updatehost(self):
		dbconn = get_conn()
		cursor = dbconn.cursor()
		sql = "UPDATE host SET type=%s,mroom=%s,status=%s,hostname=%s,app=%s,user=%s,managerip=%s,os=%s,active=%s,location=%s,produce=%s,warranty=%s,model=%s,serial=%s,cpu=%s,ram=%s,disk=%s,storage=%s WHERE ip=%s"
		cursor.execute(sql,(self.htype,self.mroom,self.status,self.hostname,self.app,self.user,self.mip,self.os,self.active,self.location,self.produce,self.warranty,self.model,self.serial,self.cpu,self.ram,self.disk,self.storage,self.ip))
		dbconn.commit()
		cursor.close()
		dbconn.close()
class Selectupdate(object):
	def selectip(self,ip):
		dbconn = get_conn()
		cursor = dbconn.cursor()
		sql = "select * from host where ip = %s"
		iptest = (ip,)
		cursor.execute(sql,iptest)
		data = cursor.fetchall()
		dbconn.commit()
		cursor.close()
		dbconn.close()
		return data
class Deldata(object):
	def delhost(self,delip):
		dbconn = get_conn()
		cursor = dbconn.cursor()
		sql = "delete from host where ip = %s"
		iptest = (delip,)
		cursor.execute(sql,iptest)
		dbconn.commit()
		cursor.close()
		dbconn.close()
