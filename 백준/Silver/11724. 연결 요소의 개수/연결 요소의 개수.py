import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(v):
    global visited
    if visited[v]==0:
        visited[v]=1
        for k in node[v]:
            dfs(k)
            
n,m = map(int,input().split())
node=[[] for _ in range(n+1)]
visited = [0]*(n+1)
visited[0]=1            # 0은 사용하지 않으므로 미리 방문처리
for _ in range(m):
    u,v = map(int,input().split())
    node[u].append(v)
    node[v].append(u)
cnt = 0
for i in range(1,n+1):
    if visited[i]==0:
        cnt +=1
        dfs(i)

print(cnt)