n = int(input("Enter the Number: "))

postive = 0
negative = 0
zero = 0

while n != -1 :
    if ( n > 0) :
        postive +=1
    elif (n == 0) :
        zero+=1
    else : 
        negative +=1

    print('Enterd Number is : ',n)
    n = int(input("Enter the Number again: "))

print('count of pos, neg, zero : ',postive,negative,zero)