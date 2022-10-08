def move_pipe(a1, b1, a2, b2):
    global cnt
    if (a2,b2)==(eni,enj):
        cnt += 1
    if (a2 - a1, b2 - b1) == (0, 1):
        ni = a2
        nj = b2 + 1
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            move_pipe(a2, b2, ni, nj)
            if 0<=ni+1<N and arr[ni + 1][nj] == 0 and arr[ni + 1][nj - 1] == 0:
                move_pipe(a2, b2, ni + 1, nj)
        else :
            return
    elif (a2-a1,b2-b1)==(1,0):
        ni = a2 + 1
        nj = b2
        if 0<= ni < N and 0<=nj < N and arr[ni][nj]==0:
            move_pipe(a2,b2,ni,nj)
            if 0<=nj+1<N and arr[ni][nj+1]==0 and arr[ni-1][nj+1]==0:
                move_pipe(a2,b2,ni,nj+1)
    else :
        if 0<=a2+1<N and arr[a2+1][b2]==0:
            move_pipe(a2,b2,a2+1,b2)
        if 0<=b2+1<N and arr[a2][b2+1]==0:
            move_pipe(a2,b2,a2,b2+1)
        if 0<=a2+1<N and 0<=b2+1<N and arr[a2+1][b2+1]==0 and arr[a2][b2+1]==0 and arr[a2+1][b2]==0 :
            move_pipe(a2,b2,a2+1,b2+1)




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
eni, enj = N - 1, N - 1
cnt = 0
move_pipe(0,0,0,1)
print(cnt)