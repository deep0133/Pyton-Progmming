print("Welcome in python")
from graphics import *

print("Enter the Radius of a circle : ")
r = int(input())

p = 3 - 2*r

# center of circle:
xn = yn = 150

x1 = 0
y1 = r

win = GraphWin("Bresenham-circle-draw",500, 500) 

plt = Point(xn+x1,yn+y1)
plt.draw(win)
plt = Point(xn+y1,yn+x1)
plt.draw(win)
plt = Point(xn+x1,yn-y1)
plt.draw(win)
plt = Point(xn+y1,yn-x1)
plt.draw(win)
plt = Point(xn-x1,yn-y1)
plt.draw(win)
plt = Point(xn-x1,yn+y1)
plt.draw(win)
plt = Point(xn-y1,yn+x1)
plt.draw(win)
plt = Point(xn-y1,yn-x1)
plt.draw(win)

while x1 < y1 :

    if p < 0 :
        p = p + 4*x1 + 6

    else :
        y1 = y1 - 1
        p = p + 4*(x1-y1) + 10
      
    x1 = x1+1  

    if x1 < y1 :
        plt = Point(xn+x1,yn+y1)
        plt.draw(win)
        plt = Point(xn+y1,yn+x1)
        plt.draw(win)
        plt = Point(xn+x1,yn-y1)
        plt.draw(win)
        plt = Point(xn+y1,yn-x1)
        plt.draw(win)
        plt = Point(xn-x1,yn-y1)
        plt.draw(win)
        plt = Point(xn-x1,yn+y1)
        plt.draw(win)
        plt = Point(xn-y1,yn+x1)
        plt.draw(win)
        plt = Point(xn-y1,yn-x1)
        plt.draw(win)

   

# Enter to exit:
x = int(input())