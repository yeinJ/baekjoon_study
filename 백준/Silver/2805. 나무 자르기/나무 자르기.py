'''
높이를 H로 지정했을 때, 상근이가 가져갈 수 있는 길이가 M과 같을 때를 찾는다.
parametric search 문제
시작점 0 끝점 가장 긴 나무의 길이
H는 시작점과 끝점의 절반으로 설정

'''
N, M = map(int,input().split())
height = list(map(int,input().split()))
start = 0
end = max(height)
result = 0
while start <= end :
    target = (start+end)//2
    total = 0
    for x in height :
        if x > target :
            total += x-target
    if total < M :
        end = target-1
    else :
        result = target
        start = target + 1
print(result)

