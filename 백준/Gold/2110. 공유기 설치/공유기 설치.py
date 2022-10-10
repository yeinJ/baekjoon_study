import sys
input = sys.stdin.readline
N,C = map(int,input().split())
house = [int(input()) for _ in range(N)]
house.sort() # 집 정렬
start = 1
end = house[-1]-house[0]    # 처음집과 마지막 집 사이의 거리
cnt = 0      # 공유기 사이 거리 최대
if C == 2:                  # 만일 공유기의 갯수가 2개로 주어졌다면, 생각할 것 없이 맨 뒤와 맨 앞에 배치
    print(end)
else :
    while start <= end :
        target = (start+end)//2
        count = 1       # 공유기는 맨 앞에 먼저 설치
        target_start = house[0]         # target_start(맨 처음 공유기는 무조건 맨 앞에 설치한다.)
        for x in house :
            if x - target_start >= target :     # 만약 house 에서 공유기 설치한 곳을 뺀 거리가 target보다 클 경우 공유기 설치
                count += 1                      # count += 1 해줌
                target_start = x                # target_start 값을 x로 변경
        if count >= C:                          # count 했을 때 C보다 크거나 같다면 target을 cnt에 기록
            cnt = target
            start = target +1                   # start는 target 값에서 +1
        elif count < C:
            end = target -1
    print(cnt)
