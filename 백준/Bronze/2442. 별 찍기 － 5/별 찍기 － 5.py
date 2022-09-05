N = int(input())
cnt = 1
for i in range(1,2*N,2):
    print(' '*(N-cnt) +'*'*i)
    cnt += 1