# sub2 함수 선언 및 정의 (매개 변수로 x,y 지정)
def sub2(x,y):
    # res 변수 선언 및 x - y로 초기화
    res = x-y
    return res

# res1 변수 선언 및 sub2 함수에 5,3을 인수로 넘겨 결과값으로 초기화
res1 = sub2(5,3)
# print 함수에 format을 지정하여 출력
print("res1 = {}".format(res1))

# res2 변수 선언 및 sub2 함수에 y값을 3 x값을 5로 지정하여 인수로 넘겨 결과값으로 초기화
res2 = sub2(y=3,x=5)
# print 함수에 format을 지정하여 출력
print("res1 = {}".format(res1))