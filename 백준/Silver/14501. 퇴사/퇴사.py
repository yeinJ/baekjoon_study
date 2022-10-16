N = int(input())
work = [list(map(int,input().split())) for _ in range(N)]
max_money = 0
memo = [0]*(N+1)
for i in range(N):
    if 0<=i+work[i][0]<N+1 and memo[i+work[i][0]]<memo[i]+work[i][1]:
        memo[i+work[i][0]]=memo[i]+work[i][1]
        for k in range(i+work[i][0]+1,N+1):
            memo[k]=max(memo[k],memo[i+work[i][0]])
print(max(memo))
