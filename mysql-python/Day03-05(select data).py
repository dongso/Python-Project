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
if __name__ == "__main__" :

    '''
        ## 팀장 --> 모든 권한
        create user director@'%' identified by 'P@ssw0rd';
        grant all on *.* to director@'%' with grant option;
    
        ## 일반직원 -> pyDB에는 읽기/ 쓰기, employees는 읽기만
        create user staff@'%' identified by 'P@ssw0rd';
        grant select, insert, update, delete on pyDB.* to staff;
        grant select on employees.employees to staff;
    
    
    '''
    # 1 데이터 베이스 연결
    con=pymysql.connect(host=host, user='staff', password='P@ssw0rd', db='pydb', charset='utf8')

    # 2. 커서 오픈
    cur=con.cursor()


    sql =" SELECT id, uname from navertbl"
    cur.execute(sql)
    print("== id ==== name ===== ")
    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        print(" {0:4d}    {1:10s} ".format(row[0], row[1]))

    cur.close()
#    con.commit()
    con.close()