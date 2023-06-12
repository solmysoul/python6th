# 예외가 두개 이상인 경우
try:
    numbers = int("Not a number")
except ValueError:
    print("Error: Invalid value.")
except TypeError:
    print("Error: Invalid type.")





