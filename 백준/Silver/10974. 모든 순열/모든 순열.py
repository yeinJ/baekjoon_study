def f(i,k):
    if i == k :
        print(*p)
    else :
        for j in range(k):
            if used[j]==0:
                used[j]=1
                p[i]= a[j]
                f(i+1,k)
                used[j]=0

N = int(input())
a = [i for i in range(1,N+1)]
used = [0]*(N)
p=[0]*N
f(0,N)