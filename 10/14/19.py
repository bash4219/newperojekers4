# We are going to look at approximations of Pi

# as well as looking at the math Module

print(22 / 7)
print(355 / 113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))


for sides in range(40000000, 400000000, 40000000):
    print(sides, archimedes(sides))


# see the loop above. in addition to the value of pi, print the difference

# between the values calculated by the archimedes function and by math.pi.

# how many sides does it take to make the two close?


print(math.pi)
#360000000 is the numbers of sides thst it takes to mack pi
print(archimedes(360000000))


acc = 0
for val in range(1, 6): #incereses by 1 stops at 6
    acc = acc + val


print(acc)


# Compute the sum of the first 100 even numbers
acc = 0
for val in range(0, 201, 2):
    acc = acc + val
print(acc)

# Compute the sum of the first 50 odd numbers
acc = 0
for val in range(1, 101, 2):
    acc = acc + val
print(acc)
# Compute the average of the first 100 odd numbers
acc = 0
for val in range(1, 201, 2):
    acc = acc + val / 100

print(acc)

# Write a function that returns the average of the first N numbers, where
#   N is a parameter
def averij(N):
    acc = 0
    for val in range(0, N, 1):
        acc = acc + val
    print(acc/N)

print(averij(6))
# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
def factorial(N):
    acc = 1
    for val in range(1, N+1, 1):
        acc = acc * val
    print(acc)

print(factorial(6))

# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
acc = 0
for Fibonacci in range(1, 12,):
    acc = acc + Fibonacci
print(acc)

# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.
def Fibonacci(N):
    acc = 1
    for Fibonacci in range(1, N+1):
        acc = acc + Fibonacci
    print(acc)
print(Fibonacci(9))



# A monto carlo simulation

# random numberd

import random
print(random.random())

# boolean expessions
#
#
# and, or, not


smallchield = 63.2
print(smallchield == 63.2)
loerjmanchielld = 107.93465
# and both
# or is ether
# mens oposet


# decision making skills
jaz = 20
bobwolker = 15
thimithy = 25
kenen = 0
if jaz > 20:
    if bobwolker < 50:
        kenen = 150
    else:
        kenen = 300
else:
    if thimithy > 500:
        kenen = 200
    else:
        kenen = 75
print(kenen)

dady = 75
if dady > 100:
    print("bigger than 100")
elif dady > 80:
    print("bigger than 80")
elif dady > 45:
    print("bigger than 45")
else:
    print("not bigger than much")

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(100))

import turtle
turtle.speed(.5)
def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.randrange(-100, 100) / 100
        y = random.randrange(-100, 100) / 100

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

print(showMontePi(100))