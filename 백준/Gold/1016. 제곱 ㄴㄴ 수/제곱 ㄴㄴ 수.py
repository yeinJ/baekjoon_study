import math
min_num, max_num = map(int,input().split())
num = [True]*(max_num-min_num+1)

for i in range(2,int(math.sqrt(max_num))+1):
    temp = int(math.pow(i,2))
    while temp<=max_num:
        start = int(min_num/temp)*temp
        for j in range(start ,max_num+1, temp): # 각 temp의 배수들을 지운다.
            if j < min_num: # min_num 범위가 아니면 continue
                continue
            if num[j-min_num]: # 해당 범위라면 num에 배수이므로 False 처리해주기
                num[j-min_num]=False
        temp *= i
ans = 0
for i in num:
    if i :
        ans += 1
print(ans)