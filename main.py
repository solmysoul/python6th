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
# new_set.clear()
print(new_set)

intersection_a_new = a.intersection(new_set, a, b) # 교집합
print(intersection_a_new)

union_a = a.union(new_set) # 합집합
print('union_a: ', union_a)

difference_a = a.difference(new_set) #차집합
print('difference_a: ', difference_a)

print(b.issubset(a)) # 부분집합

print(a.issuperset(b))

sym_a = a.symmetric_difference(new_set) # 대칭차집합 / 교집합을 뺀 나머지
print('symmetric_difference: ', sym_a)

