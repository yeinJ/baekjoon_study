N = int(input())
num = list(map(int,input().split()))
num.sort()
if N%2:
    print(num[N//2])
else :
    print(num[N//2-1])