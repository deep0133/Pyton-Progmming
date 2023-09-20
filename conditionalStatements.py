print('---------------------- Conditional Statements ----------------------')

# Upper and Lower case: 
l = str(input('Enter the word: '))
ans = ''

# ASCII value of A=65 and Z=90
# for i in range(65, 91):
#     if ( chr(i) == l[i-65]):
#         ans += chr(i).upper()
#     else :
#         ans += chr(i).lower()


# ASCII value of A=65 and Z=90
for i in range(0, len(l)):
    if ( ord(l[i]) >= 91 ):
        ans += l[i].upper()
    else :
        ans += l[i].lower()

print('ans : ',ans)


# if , elif , else:
print('---------------------- if else statements ----------------------')
salary = int(input('Enter the salary: '))

if(salary > 50000):
    print(f'salary = {salary} is greater than 50K')

elif (salary > 30000  and salary <= 40000):
    print(f'salary is between in 30K to 40K')
else :
    print(f'salary is less then 30K')


# Switch case:
## prompt the user to enter a number b/w 1 to 7 to display the correspond day of week

prompt =int(input('Enter the Day: '))

switch={
      1:'Monday',
      2:'Tuesday',
      3:'Wednesday',
      4:'Thursday',
      5:'Friday',
      6: 'Saturday',
      7: 'Sunday'
}

print(switch.get(prompt,'Invalid Input'))



