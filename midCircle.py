print("Welcome in python")
from graphics import *

print("Enter the Radius of a circle : ")
r = int(input())

p = 1.25 - r

# center of circle:
xn = yn = 150

x1 = 0
y1 = r

win = GraphWin("circle-draw-by-mid-point-algo",500, 500) 

plt = Point(xn+x1,yn+y1)
plt.draw(win)
plt = Point(xn+y1,yn+x1)
plt.draw(win)
plt = Point(xn+x1,yn-y1)
plt.draw(win)
plt = Point(xn+y1,yn-x1)
plt.draw(win)
plt = Point(xn-x1,yn-y1)  #hh
plt.draw(win)
plt = Point(xn-x1,yn+y1)
plt.draw(win)
plt = Point(xn-y1,yn+x1)
plt.draw(win)
plt = Point(xn-y1,yn-x1)
plt.draw(win)

while x1 < y1 :

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

    if p < 0 :
        x1 = x1 + 1
        y1 = y1
        p = p + 2*x1 + 1

    else :
        x1 = x1 + 1
        y1 = y1 - 1
        p = p + 2*(x1-y1) + 1
      

# Enter to exit:
x = int(input())