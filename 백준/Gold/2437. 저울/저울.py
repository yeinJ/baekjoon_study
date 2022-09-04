N = int(input())
chu = list(map(int,input().split()))
chu.sort()
num = 1
for i in range(0,N):
    if num < chu[i]:
        break
    num += chu[i]
print(num)