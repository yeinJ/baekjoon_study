import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num_list = list(map(int,input().split()))
num_list_sum = [0]      # 첫 합은 0 따라서 0넣어주기
sum_num = 0
for k in num_list:
    sum_num+=k      # sum_num에 num_list 계속 더해주기
    num_list_sum.append(sum_num)    # 해당 값 sum_list만들어서 넣어주기

for _ in range(m):
    i,j = map(int,input().split())
    answer = num_list_sum[j]-num_list_sum[i-1]  # i는 0보다 큼
    print(answer)       # 각 지정된 범위에서 i-1 빼기
                        # 누적 합에서 범위가 아닌 부분만 빼주면 됨