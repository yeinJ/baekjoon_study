'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오
'''
import sys
import math
input = sys.stdin.readline
def is_prime_number(n):
    array = [True for i in range(n+1)] #처음에는 모든 수를 소수라고 판별
    #에라토스테네스의 체
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j <=n:
                array[i*j]=False
                j += 1
    return [i for i in range(2,n+1) if array[i]]

m,n = map(int,input().split())
prime_number = is_prime_number(n)
for i in prime_number:
    if i>=m:
        print(i)
