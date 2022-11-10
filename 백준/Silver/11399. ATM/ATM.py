#11399 ATM
N = int(input())
P = list(map(int,input().split()))
# 가장 작은 값을 만들려면 가장 작은 값부터 정렬
P.sort()
total= 0
for i in range(1,N+1):
    total += sum(P[0:i]) 
print(total)