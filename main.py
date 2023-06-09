class Mobile:
    fp = 'yes' # 클래스 멤버 변수


realme = Mobile() # 생성자 함수
redme = Mobile()
geek = Mobile()

print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

Mobile.fp = 'no'

print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

realme.fp = 'Not Working' # 인스턴스 네임스페이스
print("===========")
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)



