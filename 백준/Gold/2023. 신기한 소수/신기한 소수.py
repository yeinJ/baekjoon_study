import math
import sys
sys.setrecursionlimit(10**9)

# def is_prime_number(n):
#     array = [True for _ in range(n+1)]
#     for i in range(2,int(math.sqrt(n))+1):
#         if array[i] == True :
#             j = 2
#             while i*j <=n :
#                 array[i*j]=False
#                 j+=1
#     return [i for i in range(2,n+1) if array[i]] # array[i]가 True 면 리스트에 담기
def find_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


n = int(input())
prime_one = [2,3,5,7]

def dfs(v):
    if len(str(v))==n:
        print(v)
    else :
        for i in range(1,10):
            if find_prime(v*10+i):
                dfs(v*10+i)

for i in prime_one:
    dfs(i)