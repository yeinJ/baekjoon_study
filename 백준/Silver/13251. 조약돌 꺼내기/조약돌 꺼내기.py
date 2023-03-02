M = int(input())            # 색의 종류
same_c = list(map(int,input().split()))
total_c = sum(same_c)       # 조약돌의 총 개수
k = int(input())            # 뽑은 k개의 조약돌
ans = 0                 # 모두 같은색상의 조약돌을 뽑을 확률
for i in same_c:
    if i < k :
        continue
    else :
        num = 1
        for j in range(k):
            num*=(i-j)
        ans += num

total_c_num = 1
for j in range(k):
    total_c_num *= (total_c-j)

print('%0.9f'%(ans/total_c_num))

