# 백준 9934
# 완전이진트리 - LVR - 중위순회

def inorder(n):
    global cnt
    if n<=N:
        inorder(n*2)
        tr[n]=tree[cnt]
        cnt += 1
        inorder(n*2+1)

K = int(input())
tree = list(map(int,input().split()))
N = len(tree)
cnt = 0
tr = [0]*(N+1)      # tr = 각 값들을 순서대로 받음.
inorder(1)

h=1
for i in range(K):      
    for j in range(2**i):
        print(tr[h], end=' ')
        h += 1
    print()