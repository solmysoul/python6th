stu = {101: 'Kim', 102: 'Lee', 103: 'Hong'}
fees = {'kim': 2000, 'lee': 3000, 'hong': 8000}
print(stu[101])
print(stu[102])
print(stu[103])

print(fees['kim'])
print(fees['lee'])
print(fees['hong'])

stu[102] = 'Python'
print(stu[102])

stu[104] = '멋쟁이사자'
print(stu[104])

del stu[102]
print(stu)

print(101 in stu)
print(102 in stu)

print(101 not in stu)
print(102 not in stu)

# stu.clear()
# print(stu)

new_stu = stu.copy()

key = (101, 102, 103)
value = '멋쟁이사자'
new_stu = dict.fromkeys(key, value)
print(new_stu)

print(stu[101])
print(stu.get(101))

print(stu.items())
print(stu.keys())
print(stu.values())
stu[104] = '멋쟁이사자'
print(stu)
stu.update({104: '멋쟁이사자2'})
print(stu)
stu.pop(104)
print(stu)
stu.setdefault(104, 'Park')
print(stu)

print(stu.popitem())
