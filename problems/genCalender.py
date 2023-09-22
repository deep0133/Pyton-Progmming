import datetime
today = datetime.date.today()

weekName = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day = today.isoweekday()

print("day ",weekName[day])

startDay = int(input("Enter the Start Day: "))
days = int(input("Enter the number of days: "))

print('--------------------------------------')
print('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
print('--------------------------------------')

weak = ''
for i in range(1,days+1):
    if( i % 7 == 0):
        weak += str(i)
        print(weak)
        weak = ''
    else:
        if(i > 9):
            weak = weak + str(i) + '  '
        else:
            weak = weak + str(i) + '   '
print(weak)