import pymysql

# Text기반 조회
## Global Variables ##
con = None # connection
cur = None # cursor
sql = "" # query string
row = None # 읽어들인 행 한개
host = "192.168.111.141"
user = "root"
pw = "1234" # MySQL password

# 1 데이터 베이스 연결
con=pymysql.connect(host=host, user=user, password=pw, db='naverDB', charset='utf8')
# 2. 커서 오픈
cur=con.cursor()


sql='create table if not exists naverTBL ( id varchar(50), uName varchar(50), email varchar(100), bornYear int)'
cur.execute(sql)

# Data 입력
sql="insert into naverTBL values('john','John Bann','john@naver.com',1990)"
cur.execute(sql)
sql="insert into naverTBL values('kim','Kim Chi','kim@naver.com',1992)"
cur.execute(sql)
sql="insert into naverTBL values('lee','Lee Pal','lee@naver.com',1988)"
cur.execute(sql)
sql="insert into naverTBL values('park','Park Su','park@naver.com',1980)"
cur.execute(sql)

# Data 조회
sql =" SELECT id, uName, email, bornYear from navertbl"
cur.execute(sql)
print("== id ==== name ===== email ==== bornYear")
while True:
    row = cur.fetchone()
    if row == None or row == "":
        break
    print(" {0:4s}    {1:10s}  {2:4s} ] {3:4d}".format(row[0], row[1],row[2],row[3]))







cur.close()
con.commit()
con.close()




