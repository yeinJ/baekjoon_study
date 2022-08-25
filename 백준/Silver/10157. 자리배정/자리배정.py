# 자리배정
C,R = map(int,input().split())
x = int(input())
arr = [[0]*C for _ in range(R)]
di = [1,0,-1,0]
dj = [0,1,0,-1]
dr,i,j = 0,0,0
if x > C*R:
    ans = 0
    print(ans)
else :
    for cnt in range(1,x+1):
        arr[i][j]=cnt
        ans = [j+1,i+1]
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj]==0:
            i,j = ni,nj
        else :
            dr = (dr+1)%4
            i,j = i+di[dr],j+dj[dr]
    print(*ans)