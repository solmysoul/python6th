a = {10, 20, 30}
a = {10, 20, 30, "멋쟁이사자", "hansol", 40}
a = {10, 20, 30, 40, 10, "멋쟁이사자", 20}

b = set()
print(type(b))

a.add(50)
a.update([10, 20, 60, 70])
print(a)
a.remove('멋쟁이사자') # 지울 값이 없으면 에러가 남
a.discard('멋쟁이사자') # remove와 동일하나 에러가 나지 않음
print(a)

new_set = a.copy()
new_set.clear()
print(new_set)
