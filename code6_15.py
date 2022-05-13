# 전역 변수 gval 선언 및 100으로 초기화
gval = 100

# function 함수 선언 및 정의
def function():
    # 함수 내에서 전역 변수 gval 선언
    global gval
    # print에 format을 지정하여 출력 (gval 지역 변수를 먼저 찾았으나 없으므로 전역 변수 gval을 출력)
    print("지역변수 gval : {}".format(gval))

# function함수 호출
function()