#2178
di,dj = [0,1,0,-1],[1,0,-1,0]
N , M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
q = [(0,0)]
visited[0][0]=1
ans = 0
while q:
    i,j = q.pop(0)
    if i==N-1 and j==M-1:
        ans = visited[i][j]
        break
    for a in range(4):
        ni = i+di[a]
        nj = j+dj[a]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visited[ni][nj]==0:
            q.append((ni,nj))
            visited[ni][nj]=visited[i][j]+1
print(ans)
