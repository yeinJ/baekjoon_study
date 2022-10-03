import sys
input = sys.stdin.readline

N,S = map(int,input().split())
Ni = list(map(int,input().split()))
cnt = 0
for i in range(1,(1<<N)):       # 부분집합에서 공집합 제외하려면 1부터 시작
    sum_n = 0
    for j in range(0,N):
        if i&(1<<j):
            sum_n += Ni[j]
    if sum_n==S:
        cnt += 1
print(cnt)
