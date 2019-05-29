import pymssql

class Connection :

    IP_ADDR = '192.168.111.130'
    DB_NAME = 'khyProject'
    USER_NAME = 'root'
    USER_PASS = '1234'

    def dbCONN(self):
        con = pymssql.connect(host=self.IP_ADDR, user=self.USER_NAME, password=self.USER_PASS, database=self.DB_NAME, charset='utf8')
        cur = con.cursor()
        return con,cur

