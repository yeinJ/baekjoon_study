
import math
def find_prime(n):
    global cnt
    array = [True for _ in range(n+1)]
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j <=n:
                array[i*j]=False
                j += 1
    return [i for i in range(2,n+1) if array[i]] # 소수 추출

def find_maybeprime(array): # 해당 소수 배열을 통해 제곱수 범위 출력
    global cnt
    for n in array:
        j = 2
        while math.pow(n,j) <= max_num:
            if math.pow(n,j)>=min_num: # 만약 소수의 제곱이 max_num보다 작고 min_num 보다 크다면 cnt+=1 해준다.
                cnt += 1 # 해당 값은 소수의 제곱이므로 중복될 수 없다. 따라서 리스트로 담지 않고 count 해줌
            j += 1

min_num, max_num = map(int,input().split())
cnt = 0
array=find_prime(int(math.sqrt(max_num))+1)
find_maybeprime(array)

print(cnt)
