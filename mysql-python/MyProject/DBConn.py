import pymysql

class Connection :

    IP_ADDR = 'localhost'
    DB_NAME = 'dbProject'
    USER_NAME = 'root'
    USER_PASS = 'root'

    def dbCONN(self):
        con = pymysql.connect(host=self.IP_ADDR, user=self.USER_NAME, password=self.USER_PASS, database=self.DB_NAME, charset='utf8')
        cur = con.cursor()
        return con,cur

