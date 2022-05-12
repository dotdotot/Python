# my_divmod함수 선언 및 정의
def my_divmod(n1,n2):
    # quot, rem 변수 선언 및 몫과 나머지로 초기화
    quot = n1 // n2
    rem = n1 % n2
    # tuple로 quot, rem 반환
    return (quot,rem)

# quot, rem 변수 선언및 my_divmod함수에 10,3을 인수로 넘겨 return 받은 값으로 초기화
quot, rem = my_divmod(10,3)
# print함수에 format을 지정하여 출력
print("몫 : {} 나머지 = {}".format(quot,rem))