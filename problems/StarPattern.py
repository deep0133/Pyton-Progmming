n = int(input("Enter the length of triangle: "))

for row in range(1,n+1):
    str = ''
    for col in range(0,row):
        str += '* '
    print(str)