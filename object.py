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
            