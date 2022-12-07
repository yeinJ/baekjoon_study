'''
DFS로 탐색한 결과
BFS로 탐색한 결과 출력
'''

n,m,v = map(int,input().split()) # n:정점의 개수, m:간선의 개수, v: 탐색 시작할 번호
node=[[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,input().split()) # 간선이 연결하는 두 번호 - 양방향
    node[a].append(b)
    node[b].append(a)
visited=[False]*(n+1)
dfs_list = []
for i in node:
    i.sort()


# dfs
def dfs(v):
    global dfs_list
    visited[v]=True
    dfs_list.append(v)
    for i in node[v]:
        if not visited[i]:
            dfs(i)
dfs(v)

# bfs
bfs_list = [v]
from collections import deque
q=deque()
q.append(v)
visited[v]=False
while q:
    start=q.popleft()
    for i in node[start]:
        if visited[i]:
            bfs_list.append(i)
            visited[i] = False
            q.append(i)


print(*dfs_list)
print(*bfs_list)