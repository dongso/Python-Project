def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#module1에서 실행하면 __name__이라는 특수한 변수에는 값이 __main__이 저장된다.
#하지만, 다른 파일에서 module1을 실행하면 __name__이라는 특수한 변수에는 값이
#__module1__이라는 값이 저장됨

if __name__ == "__main__":  ##해당 파일 안에서만 동작하는 코드
    print(add(3,4))
    print(sub(3,4))