'''
민호가 임의로 만든 길이 S
'''
import sys
input = sys.stdin.readline
s,p = map(int,input().split())
dna = input()
dna_name = ['A','C','G','T']
dna_num = list(map(int,input().split()))
needs=dict(zip(dna_name,dna_num))
i= 0
answer = 0
for b in range(p-1):
    needs[dna[b]]-=1
# 기본 딕셔너리 값 구하기

for a in range(s-p+1):
    needs[dna[i+p-1]]-=1
    cnt = 0
    for h in needs.values():
        if h>0:
            break
        else :
            cnt += 1
    if cnt == 4:
        answer += 1
    needs[dna[i]]+=1
    i+=1

print(answer)