import sys
import math
input = sys.stdin.readline
def find_prime(n):
    array = [True for _ in range(n+1)] # 처음에는 모든 수를 소수로 판별
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j<=n:
                array[i*j]=False
                j+=1
    return [i for i in range(2,n+1) if array[i]]

def palindrome(word):
    if word==word[::-1]:
        return True
    else :
        return False

n = int(input())
primenum=find_prime(1003002)
for i in primenum:
    if i>=n and palindrome(str(i)):
        print(i)
        break