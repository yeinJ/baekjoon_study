N,M = map(int,input().split())
mi_list = []
for i in range(N):
    Mi=list(map(int,input()))
    mi_list.append(Mi)

for h in range(N):
    for j in range(M):
        print(mi_list[h][M-j-1], end='')
    print()