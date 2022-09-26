import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
test = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())        # 초, i,j
num_list = deque()

for h in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if test[i][j]==h:
                num_list.append((i,j,0))

di = [0,1,0,-1]
dj = [1,0,-1,0]
cnt = 0

while num_list:
    i,j,time=num_list.popleft()
    if time == S:
        break
    for h in range(4):
        ni = i + di[h]
        nj = j + dj[h]
        if 0 <= ni < N and 0 <= nj < N and test[ni][nj] == 0:
            test[ni][nj] = test[i][j]
            num_list.append((ni,nj,time+1))

print(test[X-1][Y-1])