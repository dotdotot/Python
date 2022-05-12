from math import radians
from turtle import circle


# caclCircum 함수 선언 및 정의
def calcCircum(radius):
    c = 3.14 * 2 * radius
    return c

# radius 변수 선언 초기화 (초기화는 사용자에게 값을 입력받음)
radius = int(input("반지름을 입력하세요 : "))
# circum 변수 선언 및 초기화
# 초기화는 calcCircum 함수를 호출하여 초기화한다 (인수로 radius를 넘긴다)
circum = calcCircum(radius)
# print 함수 호출 및 format을 지정하여 출력
print("원주 = {}".format(circum))