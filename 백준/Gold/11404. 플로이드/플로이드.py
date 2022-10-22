'''
n개의 도시
한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스
도시의 쌍 (A,B)에 대하여 도시 A에서 B로 가는데 필요한 비용의 최솟값 구하기
도시의 개수 n , 버스의 개수 m
시작도시 a, 도착도시 b, 한 번 타는데 필요한 비용 c
'''
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
city = [[INF]*(n) for _ in range(n)]      # city n*n 판을 만들고 모두 INF 처리

for i in range(n):                      # city에서 1->1 2->2 각 자신의 위치로 가는 것은 0처리
    city[i][i]=0


for _ in range(m):
    a,b,c = map(int,input().split())
    if city[a-1][b-1]>c:
        city[a-1][b-1]=c                        # city a,b 위치에 c비용 넣기

for k in range(n):                  # k 위치를 통한, i,j 위치의 city 가 최소라면 변경
    for i in range(n):
        for j in range(n):
            city[i][j] = min(city[i][j],city[i][k]+city[k][j])

for i in range(n):
    for j in range(n):
        if city[i][j]!=INF:
            print(city[i][j],end=' ')
        else :
            print(0, end= ' ')
    print()