# 주유소
N = int(input())
min_price = 1000000001
road = list(map(int,input().split()))
price = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    if price[i] < min_price :
        min_price = price[i]
    ans += min_price * road[i]
print(ans)
