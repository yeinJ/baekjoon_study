N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr=sorted(arr)
min_time = arr[0]
cnt = 1
for i in range(1,N):
    if min_time[1] <= arr[i][0]:
        min_time = arr[i]
        cnt += 1
    elif min_time[0]<=arr[i][0] and min_time[1]>=arr[i][1]:
        min_time = arr[i]
print(cnt)