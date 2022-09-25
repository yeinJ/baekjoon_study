import sys
input = sys.stdin.readline
from collections import deque

M,N,H = map(int,input().split())
'''
토마토가 모두 익어있는 경우 -> 0이 없는경우 (0 출력)
토마토가 익을 때까지 최소(bfs 사용) 며칠이 걸리는가
모든 경우 중, 가장 먼저 끝나는 경우를 대입해야 함
불가능한 경우라면 -1 ex. 익지 않는 토마토 주위에 익은 토마토가 닿을 수 없을 때
'''

arr=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
q=deque([])
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                q.append([k,i,j])

cnt = 0
di = [0, 1, 0, -1, 0, 0]
dj = [1, 0, -1, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]
while q:                    # 처음 시작하는 점 찾기
    k,i,j=q.popleft()
    for h in range(6):
        ni = i + di[h]
        nj = j + dj[h]
        nk = k + dk[h]
        if 0 <= ni < N and 0 <= nj < M and 0<=nk<H and arr[nk][ni][nj] == 0:
            visited[nk][ni][nj] = visited[k][i][j] + 1
            q.append([nk,ni,nj])
            arr[nk][ni][nj]=1

for k in range(H):
    for i in range(N):    # bfs 다 돌았는데 아직 0이 남아있다면, 못 도는 것임
        if 0 in arr[k][i]:
            cnt = -1
            break
        if cnt < max(visited[k][i]):
            cnt = max(visited[k][i])
    if cnt == -1:
        break

print(cnt)
