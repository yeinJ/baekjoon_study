N,K = map(int,input().split())
money = []
for _ in range(N):
    Ai=int(input())
    money.append(Ai)

give=0
for i in sorted(money,reverse=True):
    if K//i >= 1:
        give += (int(K//i))
        K%=i

print(give)