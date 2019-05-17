import pymysql
#192.168.111.141

# 1 데이터 베이스 연결
con=pymysql.connect(host='#', user='root', password='1234',db='pydb', charset='utf8')

# 2. 커서 오픈
cur=con.cursor()


try :
    sql='create table naverTBL ( id int, uname char(8))'
    cur.execute(sql)
except :
    pass


sql="insert into naverTBL values(1, '홍길동')"
cur.execute(sql)
sql="insert into naverTBL values(2, '이순신')"
cur.execute(sql)

con.commit()

sql = "select * from naverTBL"
cur.execute(sql)
rows = cur.fetchall()
print(rows)


cur.close()
con.close()