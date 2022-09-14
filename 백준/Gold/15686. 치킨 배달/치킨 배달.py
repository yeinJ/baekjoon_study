import itertools
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# M 은 남은 치킨집의 개수
# N 은 도시의 크기
chicken,house = [],[] # 각 치킨집의 좌표를 구할 것
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            chicken.append([i,j])
        if arr[i][j]==1:
            house.append([i,j])

m_list = []
ans = 9999999999999999
# 치킨집의 최대 개수 M을 이용해야 한다. - M개의 치킨집 뽑기
temp = list(itertools.combinations(chicken,M))

for i in range(len(temp)):
    bns = 0
    for h in range(len(house)):
        min_road = 99999999999
        for j in range(M):
            k=abs(temp[i][j][0]-house[h][0])+abs(temp[i][j][1]-house[h][1])
            if min_road > k:
                min_road = k
        bns += min_road

    if ans > bns :
        ans = bns
print(ans)