import sys
sys.setrecursionlimit(10**6)
def dfs(v,cnt):
    global answer
    if cnt == 5:
        answer = True
        return
    visited[v]=False
    for i in friend[v]:
        if visited[i]:
            dfs(i,cnt+1)
    visited[v]=True


n,m = map(int,input().split())
friend = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

visited=[True]*(n+1)
answer = False
for k in range(n):
    dfs(k, 1)
    if answer:
        break

if answer:
    print(1)
else :
    print(0)