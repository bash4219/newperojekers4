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
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.