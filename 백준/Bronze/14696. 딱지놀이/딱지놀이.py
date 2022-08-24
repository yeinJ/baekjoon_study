# 14696 딱지놀이
N = int(input())
for _ in range(N):
    Alst,Blst = [0]*5,[0]*5
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(1,A[0]+1):
        Alst[A[i]] += 1
    for i in range(1,B[0]+1):
        Blst[B[i]] += 1

    cnt = 0
    for k in range(4,0,-1):
        if Alst[k]>Blst[k]:
            print('A')
            break
        elif Alst[k]<Blst[k]:
            print('B')
            break
        else :
            cnt += 1
            if cnt == 4:
                print('D')
                break
