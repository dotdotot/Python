# countPrimes함수 선언 및 정의
def countPrimes(endNum):
    # 2 ~ endNum-1 수 중 endNum % 를 하였을 때 나머지가 0인 개수를 cnt에 담는다
    cnt = 0
    for n in range(2,endNum):
        if isPrime(n) == True:
            cnt += 1
    return cnt

# isPrime 함수 선언 및 정의
def isPrime(num):
    # 소수라면 False를 실수라면 True를 반환
    for n in range(2,int(num/2) + 1):
        if num % n == 0:
            return False
    return True

# enum변수 선언 및 사용자에게 입력받아 초기화
enum = int(input("1부터 범위를 나타내는 끝 정수를 입력하세요"))
# cnt 변수 선언 및 countPrimes함수에 enum을 인수로 넘겨 초기화
cnt = countPrimes(enum)
# print에 format을 지정하여 출력
print("소수의 개수는 {}개".format(cnt))