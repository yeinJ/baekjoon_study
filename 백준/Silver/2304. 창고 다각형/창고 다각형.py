# 창고 다각형
N = int(input())
M=[list(map(int,input().split())) for _ in range(N)]
Mj=sorted(M)
Max_Mj,bMax_Mj = 0,0
front,back = [],[]
for i in range(N):
    if Max_Mj < Mj[i][1]:
        Max_Mj = Mj[i][1]
        front.append(Mj[i])
    if bMax_Mj < Mj[N-i-1][1]:
        bMax_Mj = Mj[N-i-1][1]
        back.append(Mj[N-i-1])

hap = 0
for i in range(len(front)):         # 최댓값 앞 부분
    if i < len(front)-1:
        hap+=(front[i+1][0]-front[i][0]) * front[i][1]

for i in range(1,len(back)):        # 최대값 기준 뒷 부분
    hap += (back[i-1][0]-back[i][0]) * back[i-1][1]

if back[-1][0]- front[-1][0] >0 :
    hap += (back[-1][0]-front[-1][0]+1)*Max_Mj
else :
    hap += Max_Mj


print(hap)