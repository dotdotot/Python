from operator import le


# calAvg함수 선언 및 정의
def calcAvg(nlist):
    avg = 0
    # len(nlist)만큼 반복하는 반복문
    # index 0번부터 차례대로 num에 들어가게된다.
    for num in nlist:
        # avg의 기존값에 num을 더하여 avg를 초기화시킨다
        avg += num
    # 평균 값을 구한다.
    avg = avg / len(nlist)
    return avg

# nlist 선언 및 초기화
nlist = [1,3,5,7,9]
# avg 선언 및 calcAvg함수에 nlist를 인수로 넘겨 결과값으로 초기화
avg = calcAvg(nlist)
# print 함수 호출 및 format을 지정하여 출력
print("평균 = {}".format(avg))