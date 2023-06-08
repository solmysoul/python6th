b = (10)
c = (10,)
print(type(b))
print(type(c))

d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, '멋쟁이사자')
f = 10, 20, -50, 21.3, '멋쟁이사자'

print(d,e,f, sep="\n")

print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])

print(f[:3])
print(f[1:4])

print(c + f)
print(f * 3)

print(10 in f)
print(-10 in f)

h = (10, 20, -50, 20)
print(min(h), max(h))

print(h.count(20))
print(h.index(20))

sorted_a = sorted(h)
print(sorted_a)

a = (10, 20, -50)
x, y, z = a
print(x, y, z)

# a와 b의 변수 바꾸기

a = 1
b = 2

tmp = a
a = b
b = tmp
print(a, b)

# 언패킹으로 변수 바꾸기

a, b = b, a
print(a, b)

list_h = list(h)
print(list_h, type(list_h))

tuple_h = tuple(list_h)
print(tuple_h, type(tuple_h))

nested_tuple = ((1,2,3), (4,5,6), (7,8,9))
print(nested_tuple)