'''
N명의 병사가 무작위로 나열되어 있다.
전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
앞에있는 병사가 전투력이 가장 높도록 배치해야 함
'''
import sys
input = sys.stdin.readline
n = int(input())
power = list(map(int,input().split()))
answer = [1]*n
power.reverse()
for i in range(1,n):
    for j in range(0,i):
        if power[j]<power[i]:
            answer[i]=max(answer[i],answer[j]+1)
print(n-max(answer))
