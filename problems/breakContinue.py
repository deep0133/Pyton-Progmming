n = int(input('Enter nth number: '))

for i in range( 1 , n+1):
    if ( i % 5 == 0):
        continue
    elif ( i == n//2):
        break
    print(i)