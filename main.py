import sys # 리미트 지정
print("default: ", sys.getrecursionlimit())
sys.setrecursionlimit(3000)
print("setting: ", sys.setrecursionlimit())

i = 0
def myfun():
    global i
    i += 1
    print("My function: ", i)
    myfun()

myfun()