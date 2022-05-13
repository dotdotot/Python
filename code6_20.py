# fibonacci 함수 선언 및 정의 (매개 변수로 받은 값을 n이라는 변수에 저장)
def fibonacci(n):
    if n == 0:
        # 종료 조건 1
        return 0
    elif n == 1:
        # 종료 조건 2
        return 1
    else:
        # 재귀 함수 호출
        return fibonacci(n-1) + fibonacci(n-2)

# 함수 호출
print(fibonacci(5))