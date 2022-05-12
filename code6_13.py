# addNums 함수 선언 및 정의 (매개변수는 n개 받는다고 지정)
def addNums(*nums):
    # 매개 변수로 받은 값 모두를 더해 return
    hap = 0
    for n in nums:
        hap += n
    return hap

# hap1 변수 선언 및 addNums에 1,2를 인수로 넘겨 결과 값으로 초기화
hap1 = addNums(1,2)
# print 함수에 format을 지정하여 출력
print("haps : {}".format(hap1))