n = int(input("Enter the number : "))

if (n <= 0 ): 
    print('-------------------Invalid Number-------------------')
    exit()

ans = 1
for i in range(1,n+1) :
    ans *= i

print("Factorial of n : ",ans)
