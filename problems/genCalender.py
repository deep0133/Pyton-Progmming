import datetime
today = datetime.date.today()

weekName = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day = today.isoweekday()

print("day ",weekName[day])

startDay = int(input("Enter the Start Day: "))
days = int(input("Enter the number of days: "))


print('--------------------------------------')
print('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
print('--------------------------------------')

# for