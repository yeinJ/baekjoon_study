N = int(input())
num_list = list(input())
a = 0
for num in num_list:        # 데이터 문자열로 받고 for문으로 돌리기
    a+=int(num)             # 문자열로 받으면 int값으로 변환시켜야함
print(a)