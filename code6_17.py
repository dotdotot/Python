# factorial함수 선언 및 정의 (매개 변수로 n을 받음)
def factorial(n):
    # n값이 0이라면 종료하도록 설정
    if n == 0:
        return 1
    # n값이 0이 아니라면 n * factorial(n-1)을 반환하도록 설정
    else:
        return n * factorial(n-1)

# ft 변수 선언 및 factorial함수에 4라는 인수를 넘겨 결과 값으로 초기화
ft = factorial(4)
# print에 format을 지정하여 출력
print("ft : {}".format(ft))

# factorial 함수는 재귀 함수이다 n값이 n값이 0이 아니라면 n * factorial(n-1)을 반환하도록 설정하고 0이라면 종료하도록 설정하였으므로
# n * n-1 * (n-1)-1 * ((n-1)-1)-1 * .... 이렇게 진행하며 n값이 0이 되는순간
# n * n-1 * (n-1)-1 * ((n-1)-1)-1 * .... * 1이 return 된다