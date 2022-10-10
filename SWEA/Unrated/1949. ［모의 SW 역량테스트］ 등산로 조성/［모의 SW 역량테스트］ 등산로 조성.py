def find_max_bong():
    max_list = []
    for i in range(N):
        for j in range(N):
            if san[i][j]==max_bong:
                max_list.append((i,j))
    return max_list

def bfs(i,j,cnt):
    global long_san
    if cnt > long_san:
        long_san = cnt
    for h in range(4):
        ni = i + di[h]
        nj = j + dj[h]
        if 0<=ni<N and 0<=nj<N and san[i][j]>san[ni][nj]:
            bfs(ni,nj,cnt+1)

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    san = []
    max_bong = 0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for _ in range(N):
        k=list(map(int,input().split()))
        san.append(k)
        max_bong = max(max_bong,max(k))
    max_list=find_max_bong()
    long_san = 0
    for i in range(N):
        for j in range(N):
            for g in range(1, K + 1):
                san[i][j] -= g
                for k in max_list:
                    if k[0]==i and k[1]==j:
                        continue
                    else:
                        bfs(k[0],k[1],1)
                san[i][j] += g
    print(f'#{tc} {long_san}')






