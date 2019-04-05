# import module1
# print(module1.add(1,2)) #module이름.함수()
# print(module1.sub(3,2))

# from module1 import * #add,sub =>* :: 모듈에 있는 모든 함수를 import, 함수 한두개를 사용할 경우에는 함수명을 입력해라
# print(add(1,2))
# print(sub(5,6))


#import module1
#여기서는 -> __name__ == __module1__

import module2
x=module2.Math() #x라는 객체 생성.
print(x.solv(2))
print(x.add(2,4))

#package: 모듈의 묶음
#패키지이름(폴더).모듈이름(파일).함수이름(함수)

#import abc.def.kkk
#abc, def는 패키지, kkk는 모듈
#abc.def.kkk.prn() ::kkk모듈에 prn이라는 함수 호출

#import abc.def.kkk as my
#my.prn() //위 호출과 같은 의미 "as my"를 써서 축약형으로 사용 가능

#from abc.def.kkk import prn
#abc.def패키지에 있는 kkk 모듈에 있는 prn 함수를 가져와라