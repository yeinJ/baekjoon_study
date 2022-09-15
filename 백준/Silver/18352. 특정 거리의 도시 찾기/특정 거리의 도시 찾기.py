from collections import deque
import sys
input = sys.stdin.readline          # 받는 값이 1만 이상일 경우 import sys 사용

def dfs(v):
    global visit
    cnt = 0
    visit[v]=99999999999999
    queue = deque([v])
    while queue:
        cnt += 1
        for h in range(len(queue)):
            a = queue.popleft()
            for i in road[a]:
                if visit[i] == 0:
                    queue.append(i)
                    visit[i]=cnt


n,m,k,x = map(int,input().split())
road = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    road[a].append(b)
dfs(x)
ans = -1
bns = []

for i in range(len(visit)):
    if visit[i]==k:
        ans = 1
        bns.append(i)
bns.sort()

if ans == -1:
    print(ans)
else :
    for i in bns:
        print(i)