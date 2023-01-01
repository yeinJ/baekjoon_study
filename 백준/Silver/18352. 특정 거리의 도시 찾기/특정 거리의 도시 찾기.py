from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split()) # n:도시의개수, m:도로의개수, k:거리정보, x:출발 도시의 번호
graph = [[] for _ in range(n+1)]
for _ in range(m): # 도로의 개수 list
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [0]*(n+1)

cnt = 0
q = deque([x]) # 시작 도시, 거리
visited[x]=1e9
while q:
    cnt += 1
    for _ in range(len(q)):
        v = q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=cnt
                q.append(i)



if k in set(visited):
    for i in range(1,n+1):
        if visited[i]==k:
            print(i)
else :
    print(-1)