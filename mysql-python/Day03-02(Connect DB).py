import sqlite3
# 1 데이터 베이스 연결
con=sqlite3.connect('C:/BigData-db/naverdb.db')

# 2. 커서 오픈
cur=con.cursor()

sql='create table if not exists naverTBL ( id int, uname char(8))'
cur.execute(sql)

sql="insert into naverTBL values(1, '홍길동')"
cur.execute(sql)
sql="insert into naverTBL values(2, '이순신')"
cur.execute(sql)

sql = "select * from naverTBL"
cur.execute(sql)
rows = cur.fetchall()
print(rows)

con.commit()

cur.close()
con.close()