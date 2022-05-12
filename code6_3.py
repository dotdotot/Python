from math import radians
from turtle import circle


def calcCircum(radius):
    c = 3.14 * 2 * radius
    return c

radius = int(input("반지름을 입력하세요 : "))
circum = calcCircum(radius)
print("원주 = {}".format(circum))