# isPrime 함수 선언 및 정의
def isPrime(num):
    # 소수라면 False를 실수라면 True를 반환
    for n in range(2,int(num/2) + 1):
        if num % n == 0:
            return False
    return True

# num 변수 선언 및 사용자에게 입력받은 값으로 초기화
num = int(input("정수를 입력하세요 : "))
# isPrime함수에 num을 인수로 넘겨 결과값을 if문의 조건식에 추가
if isPrime(num):
    # return받은 값이 True라면 print 함수에 format을 지정하여 소수라고 출력
    print("{}은 소수입니다.".format(num))
else:
    # return받은 값이 False라면 print 함수에 format을 지정하여 소수가 아니라고 출력
    print("{}은 소수가 아닙니다.".format(num))