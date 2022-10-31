import sys
input = sys.stdin.readline
n=int(input())

start = 1
end = 1
count = 0
sum_num = 1
while end<=n:
    if sum_num == n:
        count += 1
        end += 1
        sum_num += end
    elif sum_num > n :
        sum_num -= start
        start += 1
    else :
        end += 1
        sum_num += end

print(count)
