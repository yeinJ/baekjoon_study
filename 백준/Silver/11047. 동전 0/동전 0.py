'''
준규가 가지고 있는 동전은 N종류
각각의 동전을 매우 많이 가지고 있음
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 함
이때 필요한 동전 개수의 최솟값 구하기
'''

import sys
input = sys.stdin.readline
N,K = map(int,input().split()) # N : 동전의 종류 K:가치의 합
Ai = [int(input()) for _ in range(N)] # 동전의 가치
count = 0

for i in range(len(Ai)-1,-1,-1):
    if K//Ai[i]>=1:
        count+=(K//Ai[i]) # 동전의 최댓값을 이용해 몫을 구하고 해당 몫을 count에 더해준다
        # 그리고 나머지를 K로 갱신해준 후, K가 0이 될 때까지 해당 과정을 반복해준다.
        K%=Ai[i]
        
print(count)