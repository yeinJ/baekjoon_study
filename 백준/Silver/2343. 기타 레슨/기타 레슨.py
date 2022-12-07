n,m = map(int,input().split())
gt = list(map(int,input().split()))

sum_gt=sum(gt)
start,end = max(gt),sum_gt

answer = 0
while start<=end:
    mid = (start+end)//2
    cnt,num = 0,0
    for i in range(n) :
        if num+gt[i]>mid:
            # max_num=max(max_num,num-gt[i])
            cnt += 1
            num = 0
        num+=gt[i]
    if num:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid-1
        answer = mid
print(answer)
