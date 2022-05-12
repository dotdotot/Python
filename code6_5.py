# calcAvg 함수 선언 및 정의
def calcAvg(nlist):
    # nlist에 들어있는 값들의 평균을 구하는 코드
    avg = 0
    hap = calcSum(nlist)
    avg = hap / len(nlist)
    return avg

# calcSum 함수 선언 및 정의
def calcSum(nlist):
    # nlist에 들어있는 값을 모두 더해 return하는 코드
    hap = 0
    for num in nlist:
        hap += num
    return hap

# nlist 선언 및 초기화
nlist = [1,3,5,7,9]
# avg 선언 및 calcAvg함수에 nlist를 인수로 넘겨 return 받은 값으로 초기화
avg = calcAvg(nlist)
# print 함수에 format을 지정하여 출력
print("평균 = {}".format(avg))