import sys
import heapq
input = sys.stdin.readline
n = int(input())
card = []
for i in range(n):
    heapq.heappush(card,int(input()))
ans = 0
while len(card)>1 :
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)
    heapq.heappush(card,num1+num2)
    ans += (num1+num2)


print(ans)
