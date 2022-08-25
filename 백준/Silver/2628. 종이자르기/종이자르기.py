# 종이자르기
garo,sero = map(int,input().split())
N = int(input())
garo_lst,sero_lst = [0,garo],[0,sero]
for _ in range(N):
    a,b = map(int,input().split())
    if a == 1:
        garo_lst.append(b)
    else :
        sero_lst.append(b)

K,H=len(garo_lst),len(sero_lst)
garo_lst,sero_lst=sorted(garo_lst),sorted(sero_lst)
width,height = [],[]

for i in range(K-1):
    c=garo_lst[i+1]-garo_lst[i]
    width.append(c)

for i in range(H-1):
    c=sero_lst[i+1]-sero_lst[i]
    height.append(c)

Max_num = 0
for i in height:
    for j in width:
        mul=i*j
        if mul > Max_num:
            Max_num = mul
print(Max_num)
