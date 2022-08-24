N, K = map(int,input().split())
arr = [[0]*2 for _ in range(7)]
for _ in range(N):
    S,Y = map(int,input().split()) # S : 성별 남:1 여:0, Y: 학년
    arr[Y][S]+=1

sum = 0
for i in range(7):
    for j in range(2):
        if arr[i][j] !=0:
            if arr[i][j] <= K:
                sum += 1
            else :
                if arr[i][j] % K == 0:
                    sum+=(arr[i][j]//K)
                else:
                    sum+=((arr[i][j]//K)+1)


print(sum)