from itertools import combinations
from collections import deque
import copy
N = int(input())
bokdo = [list(input().split()) for _ in range(N)]
bokdo2 = copy.deepcopy(bokdo)
student=deque()
answer = 'NO'
stu_tea=deque()
for i in range(N):
    for j in range(N):
        if bokdo[i][j]=='S':
            student.append([i,j])
            for h in range(N):
                if bokdo[h][j]=='T':
                    if h>i:
                        for k in range(i+1,h):
                            if bokdo[k][j] == 'X' and [k,j] not in stu_tea:
                                stu_tea.append([k,j])
                    else :
                        for k in range(h+1,i):
                            if bokdo[k][j] == 'X' and [k,j] not in stu_tea:
                                stu_tea.append([k,j])
                if bokdo[i][h]=='T':
                    if h>j:
                        for k in range(j+1,h):
                            if bokdo[i][k]=='X' and [i,k] not in stu_tea:
                                stu_tea.append([i,k])
                    else :
                        for k in range(h+1,j):
                            if bokdo[i][k] == 'X' and [i,k] not in stu_tea:
                                stu_tea.append([i,k])


stu_safe=list(combinations(stu_tea,3))
if len(stu_tea)<3:
    stu_safe.append(stu_tea)

student2=copy.deepcopy(student)
Ne = len(student)
def conv():
    global answer,bokdo2,student2
    for u in stu_safe:
        for x,y in u:
            bokdo2[x][y]='O'
        cnt =0
        while student2:
            munja = ''
            garo_munja=''
            i,j=student2.popleft()
            for k in range(N):
                if bokdo2[i][k]=='T':
                    munja+='T'
                elif bokdo2[i][k]=='O':
                    munja+='O'
                elif bokdo2[i][k]=='S':
                    munja+='S'
                if bokdo2[k][j]=='T':
                    garo_munja+='T'
                elif bokdo2[k][j]=='O':
                    garo_munja+='O'
                elif bokdo2[k][j]=='S':
                    garo_munja+='S'
            if 'ST' not in munja and 'TS' not in munja and 'ST' not in garo_munja and 'TS' not in garo_munja :
                cnt += 1
        if cnt==Ne:
            answer='YES'
            return
        student2 = copy.deepcopy(student)
        bokdo2 = copy.deepcopy(bokdo)

conv()
print(answer)