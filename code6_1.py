# 함수 선언 및 정의
def add(x,y):
    # res 변수 선언 및 초기화
    res = x + y
    return res

# val 변수 선언 및 초기화
# 초기화는 add함수를 호출하여 return 값으로 초기화한다 (인수로 2,3을 넘긴다)
val = add(2,3)
# print에 format을 지정하여 출력
print("{} + {} = {}".format(2,3,val))

# val 변수 선언 및 초기화
# 초기화는 add함수를 호출하여 return 값으로 초기화한다 (인수로 7,8을 넘긴다)
val = add(7,8)
# print에 format을 지정하여 출력
print("{} + {} = {}".format(2,3,val))