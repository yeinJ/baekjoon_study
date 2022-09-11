#  18406 백준

num=list(input())
N=len(num)
ans1,ans2=0,0
for i in range(0,N//2):     # 값의 범위를 절반으로 나눈다. 각 자릿수의 왼,오의 합이 같아야 하기에
    ans1 += int(num[i])     # 왼쪽의 합
    ans2 += int(num[(N//2)+i])  # 오른쪽의 합
if ans1 == ans2 :
    print('LUCKY')
else :
    print('READY')