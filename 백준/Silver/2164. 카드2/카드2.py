from collections import deque
import sys
input=sys.stdin.readline
n = int(input())
cards = deque(i for i in range(1,n+1))

while len(cards)!=1:
    cards.popleft()
    num1=cards.popleft()
    cards.append(num1)

print(cards[0])