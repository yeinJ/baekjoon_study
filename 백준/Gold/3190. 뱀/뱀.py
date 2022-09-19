N = int(input())
K = int(input())
apple = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
road,dir = [0],[]
for _ in range(L):
    x,c = input().split()
    road.append(int(x))
    dir.append(c)
road.append(10000)
ni,nj = 1,1
di = [0,1,0,-1]
dj = [1,0,-1,0]
start = [[1,1]]
go,cnt = 0,0
ans = 0
for i in range(L+2):
    for j in range(road[i+1]-road[i]):
        if i == 0:
            ni=ni + di[cnt]
            nj=nj + dj[cnt]
            go += 1
            if 0<ni<=N+1 and 0<nj<=N+1 and [ni,nj] not in start:
                if [ni,nj] in apple:
                    start.append([ni,nj])
                    apple.remove([ni,nj])
                else :
                    start.pop(0)
                    start.append([ni,nj])
            else :
                ans = 's'
                break

        else :
            if j == 0:
                if dir[i-1] == 'D':
                    cnt = (cnt+1)%4
                else :
                    cnt = (cnt-1)%4
            ni = ni + di[cnt]
            nj = nj + dj[cnt]
            go += 1

            if 0<ni<N+1 and 0<nj<N+1 and [ni,nj] not in start:
                if [ni,nj] in apple:
                    start.append([ni,nj])
                    apple.remove([ni,nj])
                else :
                    start.pop(0)
                    start.append([ni,nj])
            else :
                ans = 's'
                break


    if ans=='s':
        break
print(go)










