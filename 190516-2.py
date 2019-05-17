import pymysql
from tkinter import *


## Global Variables ##
con = None  # connection
cur = None  # cursor
sql = ""  # query string
row = None  # 읽어들인 행 한개
host = "localhost"
user = "root"
pw = "1234"  # MySQL password


## Function Define ##

def searchData():
    # 1 데이터 베이스 연결
    con = pymysql.connect(host=host, user=user, password=pw, db='tabledb', charset='utf8')
    # 2. 커서 오픈
    cur = con.cursor()

    userID=edt1.get()
    sql="select b.prodName as '상품명', b.amount as '개수', (b.amount*b.price) as '총 결제 금액' from buytbl b where b.userid='"+userID+"'"
    print(sql)
    cur.execute(sql)
    prodNameList = []
    amountList= []
    priceList = []

    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        prodNameList.append(row[0])
        amountList.append(row[1])
        priceList.append(row[2])

    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)


    for pName, amount, price in zip(prodNameList, amountList, priceList):
        listData1.insert(END, pName)
        listData2.insert(END, amount)
        listData3.insert(END, price)

    cur.close()
    con.commit()
    con.close()


def insertData():
    # 1 데이터 베이스 연결
    con = pymysql.connect(host=host, user=user, password=pw, db='tabledb', charset='utf8')
    # 2. 커서 오픈
    cur = con.cursor()

    userID = edt5.get()
    prodName = edt6.get()
    pGroup=edt7.get()
    price = edt8.get()
    amount = edt9.get()

    sql = "insert into buytbl(userid, prodName, groupName, price, amount) values('"+userID+"','"+prodName+"','"+pGroup+"',"+price+","+amount+")"

    print(sql)
    cur.execute(sql)

    cur.close()
    con.commit()
    con.close()



## main ##
if __name__ == "__main__":
    window = Tk()
    window.geometry("600x300")
    window.title("GUI 데이터 입력")

    #조회 하고자 하는 아이디를 입력받는다.
    edtFrame = Frame(window)
    edtFrame.pack()

    #구매한 제품의 정보(제품명, 수량, 총 구매 금액)을 출력한다.
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    #사용자의 아이디를 입력받는다.
    edt1 = Entry(edtFrame, width=10)
    edt1.pack(side=LEFT, padx=10, pady=10)


    btnInsert = Button(edtFrame, text="구매내역조회", command=searchData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)


    #제품 이름 출력
    listData1 = Listbox(listFrame, bg='yellow')
    listData1.pack(side=LEFT, fill=BOTH, expand=1)

    #제품 수량 출력
    listData2 = Listbox(listFrame, bg='yellow')
    listData2.pack(side=LEFT, fill=BOTH, expand=1)

    # 해당 제품 구입 가격 출력
    listData3 = Listbox(listFrame, bg='yellow')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)

    edtFrame2 = Frame(window)
    edtFrame2.pack()

    #사용자 아이디 입력
    edt5 = Entry(edtFrame2, width=10)
    edt5.pack(side=LEFT, padx=10, pady=10)

    #제품명 입력
    edt6 = Entry(edtFrame2, width=10)
    edt6.pack(side=LEFT, padx=10, pady=10)

    #제품군 입력
    edt7 = Entry(edtFrame2, width=10)
    edt7.pack(side=LEFT, padx=10, pady=10)

    #제품 가격 입력
    edt8 = Entry(edtFrame2, width=10)
    edt8.pack(side=LEFT, padx=10, pady=10)

    #구매 개수 입력
    edt9 = Entry(edtFrame2, width=10)
    edt9.pack(side=LEFT, padx=10, pady=10)

    btnSelect = Button(edtFrame2, text="구매", command=insertData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    window.mainloop()



