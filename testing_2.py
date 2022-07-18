import datetime

now = datetime.datetime.now()
month = str(now.month)
day = now.strftime("%A")

print(day)

