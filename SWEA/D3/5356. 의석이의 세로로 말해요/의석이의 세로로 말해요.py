# 의석이의 세로로 말해요
T = int(input())
for tc in range(1,T+1):
    M = [[""]*16 for _ in range(16)] # 가로 세로를 넉넉하게 만들어주기
    A = [list(input()) for _ in range(5)]
    for i in range(5):
        for j in range(len(A[i])):
            M[i][j]+=A[i][j] # M이라는 새로운 공간에 A를 넣어줌

    print(f'#{tc}', end=" ")
    for k in range(16) :
        for h in range(16):
            print(M[h][k], end="")
    print()
