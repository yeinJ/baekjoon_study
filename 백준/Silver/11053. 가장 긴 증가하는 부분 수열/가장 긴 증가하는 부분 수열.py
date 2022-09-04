N = int(input())
arr = list(map(int,input().split()))
d = [0]*N
for i in range(N):
    d[i]=1
    for j in range(0,i):
        if (arr[j]<arr[i] and d[i]<d[j]+1):
            d[i] = d[j] + 1
print(max(d))