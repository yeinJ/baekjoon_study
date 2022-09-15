import sys
sys.setrecursionlimit(10**5)
from collections import deque

def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([v])
    visited[v]=False
    while queue:
        s=queue.popleft()
        print(s, end=' ')
        for i in graph[s]:
            if visited[i]:
                queue.append(i)
                visited[i]=False


n,m,v = map(int,input().split())
# N: 정점의 개수, M: 간선의 개수, V:탐색시작할 정점의 번호
graph = [[] for _ in range(10001)]
visited = [False]*(10001)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(m+1):
    if graph[i]:
        graph[i].sort()     # 작은 번호부터 찾아야 하기에 graph 정렬해줌
dfs(v)
print()
bfs(v)