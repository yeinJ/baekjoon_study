'''
n개의 음이 아닌 정수
순서를 바꾸지않고 적절히 더하거나 빼서 타겟넘버
1,1,1,1,1로 숫자 3만들기 -> 5가지 방법

'''
from collections import deque
def solution(numbers, target):
    q = deque()
    q.append((0,numbers[0]))
    q.append((0,-numbers[0]))
    answer = 0
    while q:
        i,sum_n = q.popleft()
        if sum_n == target and i==len(numbers)-1:
            answer += 1
        if i<len(numbers)-1:
            plus=sum_n+numbers[i+1]
            minus=sum_n-numbers[i+1]
            q.append((i+1,plus))
            q.append((i+1,minus))
        
    return answer