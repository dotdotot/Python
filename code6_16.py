# get_hap_diff 함수 선언 및 정의 (매개 변수로 a,b를 받음)
def get_hap_diff(a,b):
    # hap변수 선언 및 a+b로 초기화
    hap = a+b
    # 삼항 연산자 사용 
    diff = a - b if a>b else b - a
    return hap, diff

# 변수 a, b 선언 및 초기화
a = 3
b = 5
# hap, diff 변수 선언 및 get_hap_diff함수에 a,b를 인수로 넘긴 결과값으로 초기화
hap, diff = get_hap_diff(a,b)
# print에 format을 지정하여 출력
print("합 = {}, 차 = {}".format(hap,diff))