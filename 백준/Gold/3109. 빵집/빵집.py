di = [-1,0,1]
dj = [1,1,1]
def dfs(i,j,visited):
    if j==c-1:
        return True
    for h in range(3):
        ni = i + di[h]
        nj = j + dj[h]
        if 0<=ni<r and 0<=nj<c and visited[ni][nj]==0 and bread[ni][nj]!='x':
            visited[ni][nj]=1
            if dfs(ni,nj,visited):
                return True
    return False


r,c = map(int,input().split())
bread = [list(input()) for _ in range(r)]
cnt = 0
visited = [[0] * c for _ in range(r)]
for i in range(r):
    if bread[i][0]=='.':
        if dfs(i,0,visited):
            cnt +=1

print(cnt)