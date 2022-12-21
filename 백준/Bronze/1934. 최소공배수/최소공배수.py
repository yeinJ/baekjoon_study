def gcd(a,b):
    if b==0 : # b가 0이면 a가 최대공약수
        return a
    else :
        return gcd(b,a%b) # 작은수, 큰수 % 작은수

t= int(input())
for i in range(t):
    a,b = map(int,input().split())
    answer=a*b/gcd(a,b)
    print(int(answer))