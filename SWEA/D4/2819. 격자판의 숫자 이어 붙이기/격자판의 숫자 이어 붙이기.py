def what_next(i,j,number):
    global num_list
    if len(number)==7 :
        if number not in num_list:
            num_list.append(number)
            return
        else :
            return

    for h in range(4):
        ni = i + di[h]
        nj = j + dj[h]
        if 0<=ni<4 and 0<=nj<4:
            what_next(ni,nj,number+arr[ni][nj])


T = int(input())
di=[0,1,0,-1]
dj=[1,0,-1,0]
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    num_list = []
    for i in range(4):
        for j in range(4):
            number = arr[i][j]
            what_next(i,j,number)
    print(f'#{tc} {len(num_list)}')