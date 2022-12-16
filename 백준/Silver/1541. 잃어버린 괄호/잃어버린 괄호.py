exp = list(input().split('-'))
real_exp = [] # 숫자와 문자 구분할 리스트
num = 0    # 숫자를 담을 변수

for i in range(len(exp)):
    number=sum(list(map(int,exp[i].split('+')))) # +로 묶인 값들을 모두 더해준다.
    if i==0:
        num = number
    else :
        num -= number

print(num)