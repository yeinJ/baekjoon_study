import sys
input = sys.stdin.readline
from collections import deque

N,L,R = map(int,input().split())
population=[list(map(int,input().split())) for _ in range(N)]

'''
국경선을 공유하는 두 나라의 인구차이가 L명이상, R명 이하라면 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
인구수 = 연합의 인구수/연합을 이루고 있는 칸의 개수 
인접하는 나라의 차이가 L<=차이<=R일 시, 리스트에 넣기
다음 좌표도 차이가 L<=차이<=R일 시, 리스트에 넣기
다 넣어진 리스트 좌표들로 전체 값을 더해서 나누고, 해당 좌표에 넣어주기
'''


def what_neig(i, j):
    neigh= deque([(i,j)])       # neigh = 이웃한 리스트 받아주는 함수   # sum_num 처음 시작하는 값 + 연결된 모든 국가
    visited[i][j]=1
    union = [(i,j)]
    while neigh:
        i,j = neigh.popleft()
        for h in range(4):
            ni = i + di[h]
            nj = j + dj[h]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                if L<=abs(population[i][j]-population[ni][nj])<=R:
                    neigh.append((ni,nj))
                    visited[ni][nj]=1
                    union.append((ni,nj))
    return union

di = [0,1,0,-1]
dj = [1,0,-1,0]

cnt= 0
while True :
    visited = [[0] * N for _ in range(N)]
    unions =[]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = what_neig(i,j)
                if len(union)>1:
                    unions.append(union)

    if not unions:
        break

    cnt += 1

    for union in unions:
        number = sum([population[i][j] for i,j in union])//len(union)
        for i,j in union:
            population[i][j]=number


print(cnt)