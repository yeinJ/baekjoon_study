K = int(input())
K_list = []
for i in range(K):
    N = int(input())
    if N == 0:
        K_list.pop()
    else :
        K_list.append(N)
print(sum(K_list))