import matplotlib.pyplot as plt

# variables declare:



print("Enter the value of x1 : ")
x1 = int(input())

print("Enter the value of y1 : ")
y1 = int(input())

print("Enter the value of xn : ")
xn = int(input())

print("Enter the value of yn : ")
yn = int(input())

# Calculating value of delta-X and delta-Y:
deltaY = yn - y1
deltaX = xn - x1

# Calculate slop of line:
slope = deltaY / deltaX

# Decision Parameter P:
p = 2*deltaY - deltaX

# Initial point of a line:
print("(",x1,",",y1,") ")

listX = [x1]
listY = [y1]

#  checking slope condition:
if slope < 1 :
        
    while x1 < xn :

        if p < 0 :
            x1 = x1 + 1
            y1 = y1
            p = p + 2*deltaY
            listX.append(x1)
            listY.append(y1)
            print("(",x1,",",y1,") ")
            

        else :
            x1 = x1 + 1
            y1 = y1 + 1
            p = p + 2*deltaY - 2*deltaX
            listX.append(x1)
            listY.append(y1)
            print("(",x1,",",y1,") ")




else :
     while x1 < xn :

        if p < 0 :
            x1 = x1 
            y1 = y1 + 1
            p = p + 2*deltaX
            listX.append(x1)
            listY.append(y1)
            print("(",x1,",",y1,") ")
        else :
            x1 = x1 + 1
            y1 = y1 + 1
            p = p + 2*deltaX - deltaY
            listX.append(x1)
            listY.append(y1)
            print("(",x1,",",y1,") ")


# line draw of given point : [x1,x2,x3,...,xn]  ,  [y1,y2,y3,.....,yn]
plt.plot(listX,listY)

plt.show()