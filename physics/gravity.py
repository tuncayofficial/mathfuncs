import math
from sys import setswitchinterval
## Testing purposes

import math

class Object:
    def __init__(self, m, h, w, x,y):
        self.m = m
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def step_back(self, points):
         self.x -= points
            

import math

class Gravity:
    def __init__(self, m1, m2, distance, exists):
        self.m1 = m1
        self.m2 = m2
        self.g = 10
        self.distance = distance
        self.exists = exists
    
    def set_gravity(self, newG):
        self.g = newG



gravity = Gravity(5, 10, 3, True) ## G is set 10 by default for Gravity Formula
object1 = Object(5, 10, 15, 0,0)
object2 = Object(10, 5, 10, 5,0)


if(gravity.exists):
    if(object1.m > object2.m):
        for i in range(object1.x):
           object2.x += i
           print(object2.x)
