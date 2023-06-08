fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["carrot", "cucumber"]

grocery = fruits + vegetables
print(grocery)

numbers = [10, 5, 8, 1, 7]
numbers.sort() # 오름차순 정리

print(numbers)

slice_numbers = numbers[1:4]

print(slice_numbers)

numbers_copy = numbers.copy()

print(numbers_copy)

numbers_copy.pop()

print("numbers: ", numbers)

print("numbers_copy: ", numbers_copy)

numbers_clone = numbers[:]

print(numbers_clone)
