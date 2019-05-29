import DBConn


#
# obj=DBConn.Connection()
# con, cur=obj.dbCONN()
#
#
# cur.close()
# con.commit()
# con.close()

class Searching:
    obj=None
    con, cur=[None]*2#obj.dbCONN()
    sql=""
    dbTable=""

    def __init__(self):
        #생성자
        obj=DBConn.Connection()
        con,cur=obj.dbCONN()

        pass

    def __del__(self):
        #소멸자

        self.cur.close()
        self.con.commit()
        self.con.close()
        pass

    def getDBcon(self):
        return self.con,self.cur

    def getTable(self):
        return self.dbTable

    def setTable(self,tableName):
        self.dbTable=tableName
        return

    def setQuery(self, query):
        self.sql=query
        return

    def getQuery(self):
        return self.sql

    def execute(self):
        self.cur.execute(self.sql)

        print("Finish Query")
        return