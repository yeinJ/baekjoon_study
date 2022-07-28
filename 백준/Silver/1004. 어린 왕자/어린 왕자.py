T = int(input())
for _ in range(T):
    x1,y1,x2,y2=list(map(int,input().split()))
    n = int(input())
    count=0
    for _ in range(n):
        cx,cy,cr=list(map(int,input().split()))
        rou1=(x1-cx)**2+(y1-cy)**2
        rou2=(x2-cx)**2+(y2-cy)**2
        rou3=cr**2
   
        if rou3 > rou1 and rou3 > rou2:
            pass
        elif rou3 > rou1 :
            count += 1
        elif rou3 > rou2 :
            count += 1
                
    print(count)