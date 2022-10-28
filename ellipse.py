from graphics import *

# global variables:
a_sqr = b_sqr = fx = fy = d = tmp1 = tmp2 = 0


def printE():
    plt = Point(x_center+x, y_center+y)
    plt.draw(win)

    plt = Point(x_center-x, y_center+y)
    plt.draw(win)

    plt = Point(x_center+x, y_center-y)
    plt.draw(win)

    plt = Point(x_center-x, y_center-y)
    plt.draw(win)


print("********* MID POINT ELLIPSE ALGORITHM *********")

print("\n Enter coordinate x and y = ")
x_center = int(input())
y_center = int(input())

print("\n Now enter constants a and b = ")
a = int(input())
b = int(input())

win = GraphWin('Draw Ellipse', 800, 800)
x = 0
y = b
a_sqr = a*a
b_sqr = b*b
fx = 2*b_sqr*x
fy = 2*a_sqr*y
d = b_sqr-(a_sqr*b)+(a_sqr*0.25)

printE()


if d < 0:
    d = d+fx+b_sqr
else:
    y = y-1
    d = d+fx+-fy+b_sqr
    fy = fy-(2*a_sqr)

x = x+1
fx = fx+(2*b_sqr)

while fx < fy:

    printE()

    if d < 0:
        d = d+fx+b_sqr
    else:
        y = y-1
        d = d+fx+-fy+b_sqr
        fy = fy-(2*a_sqr)

    x = x+1
    fx = fx+(2*b_sqr)


tmp1 = (x+0.5)*(x+0.5)
tmp2 = (y-1)*(y-1)
d = b_sqr*tmp1+a_sqr*tmp2-(a_sqr*b_sqr)

printE()


if d >= 0:
    d = d-fy+a_sqr
else:
    x = x+1
    d = d+fx-fy+a_sqr
    fx = fx+(2*b_sqr)

y = y-1
fy = fy-(2*a_sqr)

while y > 0:

    printE()

    if d >= 0:
        d = d-fy+a_sqr
    else:
        x = x+1
        d = d+fx-fy+a_sqr
        fx = fx+(2*b_sqr)

    y = y-1
    fy = fy-(2*a_sqr)

a = int(input())
