from collections import deque
t=0
di = [0,1,0,-1]
dj = [1,0,-1,0]
while True :
    t += 1
    N = int(input())
    if N == 0 :
        break
    cage = [list(map(int,input().split())) for _ in range(N)]
    visited = [[1e9]*N for _ in range(N)]
    q=deque()
    q.append((0,0))
    visited[0][0]=cage[0][0]
    while q:
        i,j=q.popleft()
        for h in range(4):
            ni = i + di[h]
            nj = j + dj[h]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]>visited[i][j]+cage[ni][nj]:
                visited[ni][nj]=visited[i][j]+cage[ni][nj]
                q.append((ni,nj))
    print(f'Problem {t}: {visited[N-1][N-1]}')
