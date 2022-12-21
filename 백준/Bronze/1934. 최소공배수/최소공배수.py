import sys
input = sys.stdin.readline
t = int(input())
for tc in range(t):
    a,b = map(int,input().split())
    j = 2
    num_list = []
    while j<=min(a,b) :
        if a%j==0 and b%j==0 :
            a//=j
            b//=j
            num_list.append(j)
        else :
            j += 1

    ans = a*b
    for i in num_list:
        ans *=i
    print(ans)