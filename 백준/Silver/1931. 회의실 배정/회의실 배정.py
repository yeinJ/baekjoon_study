import sys
input = sys.stdin.readline
n = int(input()) # 회의의 수
time = []
for _ in range(n):
    start,end = map(int,input().split()) # start : 시작시간, end:끝나는 시간
    time.append([start,end])

time.sort(key=lambda x:(x[1],x[0]))
end_time = time[0][1]
count = 1
for i in range(1,n):
    if time[i][0]>=end_time:
        count += 1
        end_time = time[i][1]

print(count)