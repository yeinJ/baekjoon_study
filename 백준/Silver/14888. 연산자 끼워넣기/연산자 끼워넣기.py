from itertools import permutations
N = int(input())
num = list(map(int,input().split()))
ope = list(map(int,input().split()))
# 0:+, 1:-, 2:*, 3://
opera = []
for i in range(4):
    for j in range(ope[i]):     # 해당하는 oper값 개수만큼 opera에 넣어주기
        opera.append(i)
operations=list(permutations(opera,sum(ope)))       # 연산자를 통해 순열 생성

max_ans = int(-1e11)
min_ans = int(1e11)      # 10억 이상의 큰 수로 지정
for i in operations:
    ans = num[0]
    for j in range(1,N):
        if i[j-1]==0:
            ans =ans + num[j]
        elif i[j-1]==1:
            ans = ans-num[j]
        elif i[j-1]==2:
            ans = ans*num[j]
        else :
            if ans < 0 :
                ans=-(ans)//num[j]
                ans = -ans
            else :
                ans = ans//num[j]
    max_ans = max(max_ans,ans)
    min_ans = min(min_ans,ans)

print(max_ans)
print(min_ans)