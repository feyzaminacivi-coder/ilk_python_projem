from datetime import datetime
# from datetime import date
# from datetime import time

#import datetime

simdi = datetime.now()
result = simdi.day()
result = simdi.year()
result = simdi.month()
result = simdi.hour()
result = simdi.minute()
result = simdi.second()

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

# t = '21 nisan 2019'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)


t = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(dt)


birthday = datetime(1983,5,9)
print(birthday)

result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)

result = datetime.fromtimestamp(0)

result = simdi - birthday #  timedelta

print(result)
