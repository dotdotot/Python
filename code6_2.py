# rectArea 함수 선언 및 정의
def rectArea(w,h):
    # area 변수 선언 및 w * h로 초기화
    area = w*h
    return area

# area변수 선언 및 초기화
# 초기화는 rectArea함수 호출하여 return 값으로 초기화 (인수로 2,8을 넘긴다)
area = rectArea(2,8)
# print함수 호출 및 format을 지정하여 출력
print("area = {}".format(area))