# fibonacci2 함수 선언 및 정의 (매개 변수로 받은 값을 n이라는 변수에 저장)
def fibonacci2(n):
    # f(n-1)를 나타내는 변수
    prev1 = 1
    # f(n-2)를 나타내는 변수
    prev2 = 0
    for i in range(2,n+1):
        f = prev1 +prev2
        prev2 = prev1
        prev1 = f
    return f

# 함수 호출
print(fibonacci2(5))