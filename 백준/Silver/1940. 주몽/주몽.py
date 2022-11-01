def can_make(i,j,m):
    global cnt
    while True:
        closet = ingred[i] + ingred[j]
        if closet > m:
            j -= 1
        elif closet < m:
            i += 1
        else:
            cnt+=1
            j-=1
        if i>=j:
            return

import sys
input = sys.stdin.readline
n = int(input()) # 재료의 개수
m = int(input())
ingred = list(map(int,input().split()))
ingred.sort()  # 고유 번호들 정렬
i,j = 0,n-1
cnt = 0
can_make(i,j,m)
print(cnt)
