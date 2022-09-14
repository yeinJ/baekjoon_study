import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start,Tree,Par):
    for i in Tree[start]:
        if Par[i] == 0:
            Par[i]=start
            dfs(i,Tree,Par)

N = int(input())
Tree = [[] for _ in range(N+1)]
Par = [0]*(N+1)

for _ in range(N-1) :
    a,b = map(int,input().split())
    Tree[a].append(b)       # 위치 넣어주기, a에는 b를 b에는 a
    Tree[b].append(a)

dfs(1,Tree,Par)
for i in range(2,N+1):
    print(Par[i])