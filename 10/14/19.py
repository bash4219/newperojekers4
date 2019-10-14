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

for sides in range(40, 400, 40):
    print(sides, archimedes(sides))


# see the loop above. in addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# how many sides does it take to make the two close?

print(math.pi)
#360000000 is the numbers of sides thst it takes to mack pi
print(archimedes(360000000))