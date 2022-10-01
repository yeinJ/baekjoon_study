import heapq
import sys
input = sys.stdin.readline

N = int(input())
number=[int(input()) for _ in range(N)]
number.sort()
def card():
    ans = 0
    q = number
    while len(q)>=2:
        num = heapq.heappop(q)
        num2 = heapq.heappop(q)
        num3=num+num2
        ans += num3
        heapq.heappush(q,num3)
    return ans
print(card())