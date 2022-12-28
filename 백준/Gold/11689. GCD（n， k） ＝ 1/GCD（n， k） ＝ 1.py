import math
n = int(input())
# GCD = 최대공약수
# n과 서로소인 수의 개수를 구하는 문제
ans = n # n 값 복사해놓기
for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0 :   # 나눠떨어지면 n의 소인수
        while n%i == 0:     # n%i가 0이 아닐때까지 계속 돌리기
            n //= i         # 0이면 n을 i로 나눠서 다른 소인수 구하기
        ans *= 1-(1/i)      # i-1/i 를 ans에 곱해주기 -> 해당 소인수는 나눠진다.
if n>1: # n 이 1 보다 크다면 해당 n도 소인수임
    ans *= (n-1)/n 
print(int(ans))