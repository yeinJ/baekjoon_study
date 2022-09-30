def foods(i):
    global count,min_food
    if sum(count)<N//2 and i==N:
        return
    if sum(count)==N//2 :
        a_list = set()
        b_list = set()
        for j in range(N):
            if count[j]:
                a_list.add(j)
            else :
                b_list.add(j)
        one_sum = 0
        zero_sum = 0
        for j in list(a_list):
            for h in list(a_list):
                if j!=h:
                    one_sum+=food[j][h]
        for j in list(b_list):
            for h in list(b_list):
                if j!=h:
                    zero_sum+=food[j][h]
        if abs(one_sum-zero_sum) < min_food:
            min_food = abs(one_sum-zero_sum)
        return
    else :
        count[i]=1
        foods(i+1)
        count[i]=0
        foods(i+1)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    food = [list(map(int,input().split())) for _ in range(N)]
    min_food = 1e9
    count = [0]*N
    foods(0)
    print(f'#{tc} {min_food}')
