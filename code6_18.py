# factorial_iter1 함수 선언 및 정의 (매개 변수로 받은 값을 n이라는 변수에 저장)
def factorial_iter1(n):
    # prev 변수 선언 및 1로 초기화
    prev = 1
    # 1~ n만큼 반복하는 함수
    for i in range(1,n+1):
        # f라는 변수 선언 및 i * prev로 초기화
        f = i * prev
        # prev 변수를 f로 초기화
        prev = f
    return f

# num 변수 선언 및 사용자에게 입력받은 값으로 초기화
num = int(input("정수 : "))
# num 변수를 factorial_iter1 함수에 num 인수를 넘겨 결과값으로 초기화
num = factorial_iter1(num)
# print함수에 format을 지정하여 출력
print("num : {}".format(num))