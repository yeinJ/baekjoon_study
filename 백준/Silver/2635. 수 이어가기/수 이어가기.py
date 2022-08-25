# 수 이어가기
n = int(input())
Max_len= 0
for i in range(n+1):
    num = [n]
    num.append(i)
    k = 1
    while True :
        if num[k-1]-num[k]>=0:
            num.append(num[k-1]-num[k])
            k+=1
        else :
            if len(num)>Max_len:
                Max_len = len(num)
                Max_num = i
                Max_lst = num
            break

print(Max_len)
print(*Max_lst)