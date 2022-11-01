n = int(input())
Ai = list(map(int,input().split()))
Ai.sort()
good = 0
for i in range(n):
    # i는 현재 목표 값
    a,b = 0,n-1
    ans = False
    while True:
        if i==a:
            a+=1
        elif i==b:
            b-=1
        else :
            k=Ai[a]+Ai[b]
            if a>=b :
                break
            if k>Ai[i]:
                b-=1
            elif k<Ai[i] :
                a+=1
            else :
                ans = True
                break

    if ans==True:
        good +=1
print(good)

