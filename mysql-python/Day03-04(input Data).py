import pymysql

## Define Functions ##


## Global Variables ##
con = None # connection
cur = None # cursor
sql = "" # query string
row = None # 읽어들인 행 한개
host = "#"
user = "root"
pw = "1234" # MySQL password




## main ##
if __name__ == "__main__":

    # 1 데이터 베이스 연결
    con=pymysql.connect(host=host, user=user, password=pw, db='pydb', charset='utf8')

    # 2. 커서 오픈
    cur=con.cursor()


    while True:
        id=input('사용자 id : ')
        if id == "" or id == None:
            break
        uname = input('사용자 이름 : ')
        sql="insert into navertbl values("+id+", '"+uname+"')"
        cur.execute(sql)
        #print(sql)

    sql = "select * from naverTBL"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)


    cur.close()
    con.commit()
    con.close()