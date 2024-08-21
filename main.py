import calendar
from datetime import datetime

now=datetime.now()
year=now.year
month=now.month

cal = calendar.month(year, month)
print(cal)