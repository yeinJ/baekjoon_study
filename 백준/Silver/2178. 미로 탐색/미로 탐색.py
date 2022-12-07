'''
1 : 이동할 수 있는 칸
0 : 이동할 수 없는 칸
1,1 -> n,m 위치 이동 시, 지나야 하는 최소 칸 수 구하기
(최소 칸 -> bfs 이용)
'''
from collections import deque
n,m = map(int,input().split())
miro = [list(input()) for _ in range(n)] # 붙어서 주어지기에 list로 떼 줘야 함 -> str로 표시
q = deque()
q.append((0,0)) # 시작점 넣기
di = [0,1,0,-1]
dj = [1,0,-1,0] # 4 방향 표시
visited= [[1e9]*m for _ in range(n)]
visited[0][0]=1
while q :
    i,j = q.popleft()
    for h in range(4):
        ni = i + di[h]
        nj = j + dj[h]
        if 0<=ni<n and 0<=nj<m:
            if miro[ni][nj]=='1' and visited[ni][nj]>visited[i][j]+1:
                visited[ni][nj]=visited[i][j]+1
                q.append((ni,nj))
print(visited[n-1][m-1])