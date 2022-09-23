print("Welcome in python")
import matplotlib.pyplot as plt

print("Enter the Radius of a circle : ")
r = int(input())

n = i = 1

while i <= r :

    i= i*2
    n = n+1

e = 1/i
print("e : ",e)

listX = [0]
listY = [r]

x1 = xn = 0
y1 = yn = r


xn = xn + e*yn
yn = yn - e*xn

listX.append(xn)
listY.append(yn)
             
while 0.7254448318274125 != xn and -50.00040487996277 != yn :
    xn = xn + e*yn
    yn = yn - e*xn
    listX.append(xn)
    listY.append(yn)
   

print("out of while loop and list is : ",listX,listY)
plt.plot(listX,listY)
plt.show()