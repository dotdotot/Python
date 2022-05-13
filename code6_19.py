# factorial_iter2 함수 선언 및 정의 (매개 변수로 받은 값을 n이라는 변수에 저장)
def factorial_iter2(n):
    # flist 리스트 생성
    flist = []
    # flist에 초깃값 1을 추가 (n = 0일때 팩토리얼 값)
    flist.append(1)

    # 1~n만큼 반복하는 반복문
    for i in range(1,n+1):
        # flist[i - 1] * 1를 flist에 추가
        flist.append(i * flist[i-1])

    return flist

# flist 변수 선언 및 factorial_iter함수에 4를 인수로 넘겨 결과 값으로 초기화
flist = factorial_iter2(4)
# print함수에 format을 지정하여 출력
print("format = {}".format(flist))