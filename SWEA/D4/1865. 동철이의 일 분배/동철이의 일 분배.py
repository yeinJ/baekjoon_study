def success(i,suc_cnt):
    global max_suc
    if max_suc >= suc_cnt:
        return
    if i==N:
        if max_suc < suc_cnt:
            max_suc=suc_cnt
    else :
        for j in range(N):
            if count[j]==0:
                count[j]=1
                success(i+1,suc_cnt*(arr[i][j]*0.01))
                count[j]=0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    count = [0]*N
    max_suc = -1
    success(0,100)
    print(f'#{tc} {max_suc:.6f}')