from datetime import timedelta
from datetime import date
from datetime import datetime

td = timedelta(days=10)
print(td)

d1 = date(year=2023, month=5, day=5)
d2 = date(year=2023, month=6, day=9)

print(d1 == d2) # 등호 연산자에 대한 재정의
print(d1 < d2)
print(d1 > d2)

dt = datetime.today()

formated_datetime = dt.strftime('%B, %d, %Y')
print(formated_datetime)

