import sys
input = sys.stdin.readline
N = int(input())
count = [0]*2000002
for _ in range(N):
    num = int(input())
    count[num+1000000]=1

for i in range(2000002):
    if count[i]:
        print(i-1000000)

