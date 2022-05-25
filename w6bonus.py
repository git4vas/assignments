import random
from math import pi

def points_rnd(n):
    return [(random.random(), random.random()) for _ in range(n)]

coordinates = points_rnd(10000)

circle = 0

for i in range(10000):
    if (coordinates[i][0]**2 + coordinates[i][1]**2) <= 1:
        circle += 1

pi_calc = circle / 10000 * 4
print("Calculated value of π:", pi_calc)
print("Value of π from math library:", pi)
print("Difference:", pi - pi_calc)