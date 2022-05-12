# prtMultTable 함수 선언 및 정의
def prtMultTable(dan):
    # dan의 1~9까지 곱한 값을 출력하는 코드
    for i in range(9):
        print("{} * {} = {}".format(dan,i + 1,dan*(i + 1)))

# dan 변수 선언 및 사용자에게 입력받아 초기화
dan = int(input("단을 입력하세요 : "))
# prtMultTable함수에 dan을 인수로 넘겨 호출
prtMultTable(dan)