# def 함수 선언 및 정의 
# 매개변수 h는 default 값을 5로 지정
def rectArea(w,h = 5):
    # area 변수 선언 및 w * h로 초기화
    area = w*h
    return area

# area 변수 선언 및 rectArea함수에 3을 인수로 넘겨 초기화
# rectArea 함수가 받는 매개 변수는 2개이고 넘기는 인수는 1개 뿐이지만 1개의 매개 변수가 default값이 5로 지정되어 있으므로 에러가 발생하지 않음
area = rectArea(3)
# print에 format을 지정하여 출력
print("area = {}".format(area))

