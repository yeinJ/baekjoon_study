def f(i):
    global cnt
    if i==N:
        cnt +=1
    else :
        for j in range(N):
            if N_count[j]==0 and BD_line[i+j]==0 and D_line[i+N-1-j]==0:
                N_count[j]=1
                BD_line[i+j]=1
                D_line[i+N-1-j]=1
                f(i+1)
                N_count[j]=0
                BD_line[i+j]=0
                D_line[i+N-1-j]=0

N = int(input())
D_line = [0]*(N+N+1)
N_count = [0]*(N)
BD_line = [0]*(N+N+1)
cnt = 0
f(0)
print(cnt)