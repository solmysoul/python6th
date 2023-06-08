# 변수 선언
# a = 10
# b = 3.14
# c = "Hello, World!"
# d = [1, 2, 3]
# e = (4, 5, 6)
# f = {7, 8, 9}
# g = {"apple": 1, "banana": 2, "orange": 3}
#
# # 데이터 타입 출력
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
#
# # 덧셈
# a = 4
# b = 2
# total = a + b
# print('total = a + b :', total)
#
# #뺄셈
# a = 4
# b = 2
# total = a - b
# print('total = a - b :', total)
#
# #곱셈
# total = a * b
# print('total = a * b :', total)
#
# #나눗셈
# print('a / b: ', a / b)
#
# #나머지
# a = 5
# b = 2
# print('a % b: ', a % b)
#
# #거듭제곱
# print('a ** b: ', a ** b)
#
# #몫(양수)
# print('a // b: ', a // b)
#
# #몫(음수)
# a = -5
# print('-a // b: ', a // b)
#
# #========================
#
# #비교연산자
# a = 5
# b = 2
# print('a < b: ', a < b)
#
# print('a <= b: ', a <= b)
#
# print('a != b: ', a != b)
#
# print('a == b: ', a == b)

# =======================

##논리연산자
# a = 5
# b = 2
# c = 3
# d = 200
#
# print('AND 연산자')
# print('a > b and a > c: ', a > b and a > c)
#
# print('OR 연산자')
# print('a > b or a < c: ', a > b or a < c)
#
# print('NOT 연산자')
# print('not(a < b): ', not(a < b))

# #=======================

# #할당 연산자 =
# a = 10
# b = 20
# m = 15
#
# y = a + b
# print(y)
#
# m += 10
# print(m)
#
# m **= 2
# print(m)
#
# m //= 10
# print(m)

# #비트 연산자

# a = 10
# b = 15
#
# print('a: ', bin(a))
#
# print('b: ', bin(b))
#
# print('~a = ', ~a, bin(~a))
#
# print('a & b: ', a & b)
#
# print('a << 2: ', a << 2)

# #========================
#
# # 멤버 in 연산자
#
# st1 = "Welcome to 멋쟁이 사자"
# print("to" in st1)
#
# st2 = "Welcome top 멋쟁이 사자"
# print("to" in st2)
#
# st3 = "Welcome to 멋쟁이 사자"
# print("subs" in st3)
#
# st1 = "Welcome to 멋쟁이 사자"
# print("to" not in st1)
#
# st2 = "Welcome top 멋쟁이 사자"
# print("to" not in st2)
#
# st3 = "Welcome to 멋쟁이 사자"
# print("subs" not in st3)

# =============================
#
# #is 연산자
#
# a = 10
# b = 10
# print(a is b)
# print(a is not b)
#
# a = 10
# b = '10'
# print(a is b)

# # 암시적 타입 변환
#
# a = 5
# b = 2
# print(b, type(b))
# value = a / b
# print(value)
# print(type(value))
#
# x = 10
# y = 5.5
# total = x + y
# print(total)
# print(type(total))
#
# j = "Hello "
# k = "Like lion"
# p = j + k
# print(p)
# print(type(p))
#
# q = 20
# u = '10'
# r = q + u #오류
# print(r)

# # =========================
#
# # 명시적 타입 변환
# a = 5
# b = 2
# value = a / b
# print(type(value))
# int_value = int(value)
# print(int_value, type(int_value))

# q = 20
# u = '10'
# print(type(u))
# r = q + int(u)
# print(r, type(r))
# r = str(q) + u
# print(r, type(r))

# n1 = 10.36
# vn1 = int(n1)

# print(vn1, type(vn1))

# n5 = "멋쟁이 사자"
# vn5 = tuple(n5)
#
# print(vn5, type(vn5))
#
# n5 = ("kim", "Bae")
# vn5 = list(n5)
#
# print(n5, type(n5))
# print(vn5, type(vn5))

# print("1", "2", "3")
#
# print("1")
# print("2", end='')
# print("3")

# 문자열 구분자

# data = [10, 20, -50, 21.3, 'LikeLion']
# print(data)
#
# print("Like", "Share", "Subscribe")
# print("Like", "Share", "Subscribe", sep='')
# print("Like", "Share", "Subscribe", sep='**')

# print("Like", "Share", "Subscribe", sep='**', end='\t')
# print("Like", "Share", "Subscribe", sep='**', end='\t')

# ====================

# m = 40
# print("value: ", m)
#
# name = "이한솔"
# age = 26
# print("My name is", name, "and My age is", age)

# print("Welcome", end='\t')
# print("to", end='\t')
# print("LikeLion")

# name = input()
# print(name, type(name))
#
# name = input("Your Name: ")
# mobile = input("Enter Your Mobile Number: ")
# mb = int(mobile)
# print(mb, type(mb))

# price = float(input("Total Price:"))
# print(price, type(price))

# print("Hello\nWorld")
# print("Hello\tWorld")
# print("Hello\\World")
#
# print('He said, "Hello,World"')
# print("He said, \"Hello,World\"")

# # if 문
#
# x = 5
# if x > 3:
#     print("x는 3보다 큽니다.")
#
# # if else
# age = 18
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")
#
# # 중첩된 if else
#
# score = 85
# if score >= 90:
#     print("A 학점")
# else:
#     if score >= 80:
#         print("B 학점")
#     else:
#         if score >= 70:
#             print("C 학점")
#         else:
#             print("D 학점")
#
# # if elif
#
# marks = 75
# if marks >= 90:
#     print("A 등급")
# elif marks >= 80:
#     print("B 등급")
# elif marks >= 70:
#     print("C 등급")
# else:
#     print("D 등급")
#
# a = int(input("Enter Number Greater then 2:"))
# if a > 2:
#     print("You have entered:", a)
#
# a = int(input("Enter Number Greater then 2:"))
# if a >= 2:
#     print("Correct!! You have entered:", a)
# else:
#     print("Wrong!! You have entered:", a)
#
# day = input("요일을 입력하세요: ")
# if day == "Mon":
#     print("오늘은 월요일")
# elif day == "Tue":
#     print("오늘은 화요일")
# elif day == "Wed":
#     print("오늘은 수요일")
# else:
#     print("휴일")

# i = 0
# while i < 10:
#     i += 1
#     print("i: ", i)
# else:
#     print("else")
#
# while True:
#     a = input("Enter Menu Number: ")
#     if a == '0':
#         break
#     print("a: ", a)
# else:
#     print("else")

# while loop

# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# print("코드종료")

# a = 2
# while a <= 20:
#     print(a)
#     a += 2
# print("코드종료")

# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# else:
#     print("while 조건이 거짓이므로 Else 부분 실행됨")
# print("코드 종료")

# # 무한 루프
# while True:
#     print("멋쟁이 사자")
# print("코드종료")

# i = 1
# while i <= 3:
#     print("Outer Loop", i)
#     i += 1
#     j = 1
#     while j <= 5:
#         print("Inner Loop", j)
#         j += 1
# print("코드 종료 ")

# range

# for i in range(5):
#     print(i)
#
# for i in range(2,7):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(-1, -10, -2):
#     print(i)

# a = range(5)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# print("Reverse Rage with Start, stop, step")
# r = range(5, 0, -1)
# print(r[0])
# print(r[1])
# print(r[2])
# print(r[3])
# print(r[4])

# # For in

# st = "멋쟁이 사자"
# for ch in st:
#     print(ch)
# else:
#     print("Else")
#
# print("코드 종료")

# pass 문

# a = 5
# if a < 6:
#     pass
# else:
#     print("6보다 큼")

# # 배열 생성 및 원소 접근
# import array
# stu_roll = array.array('i', [101, 102, 103, 104, 105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])
#
# print("for in 사용")
# for element in stu_roll:
#     print(element)
#
# print("인덱스를 이용한 순회")
# n = len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])
#
# print("인덱스를 사용한 while 루프 배열 순회")
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# # 배열 삽입
# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("Array After Insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("Array After Remove")
#
# stu_roll.remove(107)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("Array pop()")
#
# element = stu_roll.pop()
# print("element", element)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105])
# print(stu_roll.index(105))
#
# print("extend() 메소드")
# arr = array('i', [201, 208, 210])
# stu_roll.extend(arr)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("reverse() 메소드")
# stu_roll.reverse()
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])
# print("배열 슬라이싱")
# print(stu_roll[2:3])
# print(stu_roll[0:])
# print(stu_roll[-2:])
#
# n = len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])
#
# print("1:5까지")
# a = stu_roll[1:6]
# for i in a:
#     print(i)
#
# print("0번째 부터 끝까지")
# b = stu_roll[0:]
# for i in b:
#     print(i)
#
# print("처음부터 5번째까지")
# c = stu_roll[:6]
# for i in c:
#     print(i)
#
# print("마지막 요소 4개")
# d = stu_roll[-4:]
# for i in d:
#     print(i)
#
# print("0부터 6번째까지 2개씩 건너 뛰어 출력")
# e = stu_roll[0:7:2]
# for i in e:
#     print(i)
#
# print("마지막 5개의 요소 중 오른쪽으로부터 2개의 요소를 출력")
# f = stu_roll[-5:-3]
# for i in f:
#     print(i)

# str1 = 'LikeLion'
# str2 = "LikeLion"
# str3 = '''
# 동해물과 백두산이
# 마르고 닳도록
# 하느님이 보우하사
# 우리나라 만세
# '''
# str4 = """
# 동해물과 백두산이
# 마르고 닳도록
# 하느님이 보우하사
# 우리나라 만세
# """
#
# print(str1)
# print(str2)
# print(str3)
# print(str4)
#
# str5 = 'Hello "Like Lion" How are you'
# str6 = "Hello 'Like Lion' How are you"
#
# print(str5)
# print(str6)
#
# str7 = "Hello \nHow are you?"
# str8 = "Hello \\nHow are you?"
# str9 = r"Hello \nHow are you?"
#
# print(str7)
# print(str8)
# print(str9)

# s = "Hello World"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.isupper())
# print(s.islower())
# print(s.istitle())
# print(s.isdigit())
# print(s.isalpha())

# s = " Hello World "
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# s = "Hello, World"
# print(s.replace("World", "there"))
# print(s.replace("world".title(), "there"))
# split_str = s.split(",")
# print(split_str)
# print(" ".join(split_str))
#
# print(s.startswith("Hello"))
# print(s.endswith("World"))

# print("인자가 없는 함수")
# def disp():
#     name = "멋쟁이 사자"
#     print("Welcome to", name)
#
# print("함수 실행")
# disp()
# disp()
# disp()
#
# def add():
#     x = 10
#     y = 20
#     c = x + y
#     print(c)
#
# add()
#
# def add(y):
#     x = 10.234
#     print(x + y)
#     print(f"Formatted Output {x + y:5.2f}")
# add(20)

# print("반환")
# def add():
#     x = 10
#     y = 20
#     c = x + y
#     return c
#
#
# sum1 = add()
# print(sum1)
#
# def add2():
#     x = 10
#     y = 20
#     return x + y
#
#
# sum2 = add2()
# print(sum2)
#
# def add(y):
#     x = 10
#     return x + y
#
#
# sum3 = add(20)
# print(sum3)
#
# def add(y):
#     x = 10
#     c = x + y
#     d = y - x
#     return c, d, 50
#
# sum4, sub1, a = add(20)
# print(sum4)
# print(sub1)
# print(a)

# def disp():
#     def show():
#         print("Show Function")
#     print("Disp Function")
#     show()
#
# disp()
#
# def disp():
#     def show():
#         return "Show Function"
#     result = show() + "Disp Function"
#     return result
#
# print(disp())

# def disp(sh):
#     print(type(sh))
#     print("Disp function" + sh())
#
# def show():
#     return " Show Function"
#
# disp(show)

# def disp():
#     def show():
#         return "Show Function"
#     print("Disp Function")
#     return show
#
# r_sh = disp()
# print(r_sh(), type(r_sh))

# def disp(sh):
#     print("Disp Function")
#     return sh
#
# def show():
#     return "Show Function"
#
# r_sh = disp(show)
# print(r_sh())
# print(show())

# ========== 2023 06 08 2교시 ============
# print("위치를 가진 인수")
# def pw(x, y):
#     z = x ** y
#     print(z)
#
# pw(2, 5)
# pw(5, 2, 3) #함수 인자가 2개만 되는 경우에는 3개를 넣었을 시 오류

print("키워드 인자")


def show(name, age):
    print(f"Name: {name} Age: {age}")  # 선언부


show(name="멋쟁이사자", age=26)  # 함수파라미터를 키워드로 전달해서 순서 상관없이 실행할 수 있다. # 호출부
# 모든 키워드 값을 넣지 않았을 시 실행이 되지 않는 오류 발생
# 위와 같은 오류를 방지하기 위해 함수에 기본 값을 넣어줌
# def show(name, age=27):


# 컴파일 언어는 짠 코드를 특정 시점에 컴파일러가 파악해서 기계어로 변환
# 스크립트 언어는 인터프리터를 가지고 있음, 인터프리터는 변환과정이 하나 더 있음, 입력한 코드를 구문 분석 후 재배치한 후 실행,
# 즉 좀 더 유연함


print("Example 1")


def add(x, y):
    z = x + y
    print("Addition: ", z)


add(5, 2)

print("Example 2")


def add(*num):  # *을 사용하면 여러개의 값을 넣을 수 있음
    z = num[0] + num[1] + num[2]
    print("Addition *: ", z)


add(5, 2, 4)

print("Example 3")


def add(x, *num):
    z = x + num[0] + num[1]
    print("Addition x *: ", z)


add(5, 2, 4)

# command + option + L  자동서식지정 (들여쓰기 등)
