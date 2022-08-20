# 색종이
N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            arr[i][j] = 1

sum_a = 0
for i in range(101):
    for j in range(101):
        sum_a += arr[i][j]

print(sum_a)