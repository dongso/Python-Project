#Dictionary :: Key(변하지 않는 값)와 Value(변하는/변하지 않는 값)의 쌍으로 데이터를 표현하는 자료구조
#DictionaryName={Key:Value, ...}
#score={'kor':90}  => Key : 'kor', Value=90
#'key'::''를 사용해 key임을 나타내준다(문자열) , ''를 쓰지 않으면 변수.
#key-value의 대응은 1:1
score={'kor':90, 'eng':90, 'mat':70, 'kor':100}
print(score)

a={1:'hi'} #key:1, value:'hi'
a={1:'hi', True:'hello'} # 1과 True가 중복!
a={1:'hi', False: 'hello'} # key:False, Value:'hello', 실제로 이런식으로 안씀
a={1:'hi', False: 'hello', 3.14:[1.5,2.5]} # Key에는 숫자, 불린 모두 올 수 있다.
print(a)

#b= {[1,2]:100} #unhashable type::키에는 list가 올 수 없다.
#c={{'a':1}:200} #unhashable type::Key에 Dictionary가 올 수 없다.