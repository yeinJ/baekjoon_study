import sys
input=sys.stdin.readline


T = int(input())
memo_zero = [0]*41
memo_one = [0]*41
memo_zero[0]=1
memo_zero[1]=0
memo_one[0]=0
memo_one[1]=1
for i in range(2,41):
    memo_one[i]=memo_one[i-1]+memo_one[i-2]
    memo_zero[i]=memo_zero[i-1]+memo_zero[i-2]
for _ in range(T):
    N=int(input())
    print(memo_zero[N],memo_one[N])