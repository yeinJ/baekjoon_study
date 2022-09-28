from collections import deque

def bfs():
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    while tomato:
        i,j=tomato.popleft()
        for h in range(4):
            ni = i + di[h]
            nj = j + dj[h]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0:
                visited[ni][nj]=visited[i][j]+1
                tomato.append((ni,nj))


M,N = map(int,input().split())
box=[list(map(int,input().split())) for _ in range(N)]
'''
익은 토마토 1, 익지 않은 토마토 0, 토마토 안 들어있음 -1
'''
tomato = deque()
answer = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            visited[i][j]=1
            tomato.append((i,j))
        if box[i][j]==-1:
            visited[i][j]=-100

bfs()
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            answer = -1
            break
    if answer==-1:
        break
    answer=max(max(visited[i]),answer)
if answer==-1:
    print(answer)
else :
    print(answer-1)