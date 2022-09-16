def inorder(n,level):
    global ans
    if n:
        level += 1
        inorder(ch1[n],level)
        ans.append(level)
        inorder(ch2[n],level)

def findroot():
    for i in range(1,N+1):
        if par[i]==0:
            return i

N = int(input())
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
ans=[0]
par = [0]*(N+1)

for _ in range(N):
    a, al, ar = map(int,input().split())
    if al != -1:
        par[al]=a
        ch1[a]=al
    if ar != -1:
        ch2[a]=ar
        par[ar]=a


inorder(findroot(),0)
max_level = max(ans)
# for i in range(1,len(ans)):
#     max_level=max(ans[i],max_level)
max_gap = 0
max_le = 0
for i in range(1,max_level +1):
    min_ans, max_ans = 99999999999999999999999999999, 0
    for j in range(1,len(ans)):
        if ans[j]==i:
            min_ans=min(min_ans,j)
            max_ans=max(max_ans,j)
    if max_gap < max_ans-min_ans+1:
        max_gap = max_ans-min_ans+1
        max_le = i
print(max_le,max_gap)