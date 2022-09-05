# 1475 방번호
N = list(map(int,input()))
arr = [0]*9
for i in N :
    if i == 9 :
        arr[6] += 1
    else :
        arr[i] += 1
if arr[6] % 2:
    arr[6]=(arr[6]//2+1)
else :
    arr[6]=arr[6]//2
print(max(arr))