def pre(n):
    if n :
        print(chr(n+64), end='')
        pre(ch1[n])
        pre(ch2[n])

def inorder(n):
    if n :
        inorder(ch1[n])
        print(chr(n+64),end='')
        inorder(ch2[n])

def postorder(n):
    if n :
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n+64), end='')

N = int(input())
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
for _ in range(N):
    node,son1,son2 = input().split()
    if son1 != '.':
        ch1[ord(node)-64]=ord(son1)-64  # node의 좌측
    if son2 != '.':
        ch2[ord(node)-64]=ord(son2)-64  # node의 우측

pre(1)
print()
inorder(1)
print()
postorder(1)
print()