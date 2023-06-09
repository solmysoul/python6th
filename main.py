import time # import 에서 해당 기능을 가져옴
from datetime import datetime
from datetime import date

print(time.time())
print(time.ctime())


dt = datetime(year=2023, month=5, day=5, hour=10, minute=30)
print(dt)
print(type(dt))

current_datetime = datetime.now()
print(current_datetime)

current_ctime = time.ctime()
print(current_ctime)

d = date(year=2023, month=6, day=25) # 시간 정보 없이 날짜만
print(d)

current_date = date.today() # 시간 정보 없이 현재 날짜만
print(current_date)



