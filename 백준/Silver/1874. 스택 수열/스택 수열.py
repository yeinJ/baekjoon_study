'''
1-n까지 수 스택에 넣었다가 뽑아 늘어놓기
하나의 수열 만들기
스택 push 순서 오름차순
1-n에서 차례대로 push 로 리스트 넣기
만일 원하는 값이 나왔다면 pop
다시 넣기
다시 넣는 과정 중, 불가능 하다면 NO 출력
'''
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
answer = deque(int(input()) for _ in range(n))
num = []
ans = []
i ,j= 1,0
while i<=n:
    if i<=answer[j]:
        num.append(i)
        ans.append('+')
    else :
        ans = 'NO'
        break
    k = 0
    if i == answer[j]:
        while num:
            if num[-1]==answer[j]:
                num.pop()
                answer.popleft()
                ans.append('-')
                k+=1
            elif num[-1]!=answer[j] and n==i:
                ans = 'NO'
                break
            elif num[-1]!=answer[j]:
                break

    if ans =='NO':
        break
    i+=1

if ans=='NO':
    print(ans)
else :
    for i in ans:
        print(i)








