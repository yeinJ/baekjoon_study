import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
A,B = map(int,input().split())
distance = [INF]*(N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        d,n = heapq.heappop(q)
        if distance[n]<d:
            continue
        for dis,cost in graph[n]:
            cost+=d
            if cost<distance[dis]:
                distance[dis]=cost
                heapq.heappush(q,(cost,dis))

dijkstra(A)
print(distance[B])
