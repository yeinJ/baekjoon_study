N = int(input())

# 카운트 정렬 쓰기
count=[0]*20000002
num = map(int,input().split())
for h in num:
    count[h+10000000]+=1
M = int(input())
find_list = [0]*M
M_list = list(map(int,input().split()))
for h in range(M):
    find_list[h]=count[M_list[h]+10000000]
print(*find_list)