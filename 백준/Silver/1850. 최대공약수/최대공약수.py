import sys
input = sys.stdin.readline
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())
num = gcd(a,b)


for i in range(num):
    print(1, end='')