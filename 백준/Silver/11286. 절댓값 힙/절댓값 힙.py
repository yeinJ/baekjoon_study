import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    target = int(input())
    if target==0:
        if array:
            ab_num,num=heappop(array)
            print(num)
        else :
            print(0)
    else :
        heappush(array,(abs(target),target))
        