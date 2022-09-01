S = list(map(int,input()))

cnt_0 = 0
cnt_1 = 0
if S[0]:
    cnt_1 += 1  # 첫번째 index가 1 일 경우
else:
    cnt_0 += 1  # 첫번째 index가 0일 경우

for i in range(len(S)):
    if i-1>=0:
        if S[i]==1 and S[i-1]==0:
            cnt_1 += 1
        if S[i]==0 and S[i-1]==1:
            cnt_0 += 1
if cnt_1 > cnt_0 :
    ans = cnt_0
else :
    ans = cnt_1
print(ans)