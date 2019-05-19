import pymssql

db = "bigDB"
host = "192.168.111.130"
user = "root"
password = "1234"

con = pymssql.connect(server=host, user=user, password=password, database=db)
cur= con.cursor()

sql="select *from bigTBL"

cur.execute(sql)

while True:
    row=cur.fetchone()
    if row == "" or row == None:
        break

    print(row[0], row[1])




cur.close()
con.close()









