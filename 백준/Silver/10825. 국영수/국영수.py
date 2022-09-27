'''
1. 국어점수가 감소하는 순서(내림차순)
2. 국어 같을 시, 영어 증가하는 순서(오름차순)
3. 국어,영어 같을 시, 수학 감소하는 순서
4. 모두 같으면 이름이 사전 순으로 오름차순
'''

N = int(input())
name_list=[]
for i in range(N):
    name,ko,en,ma = input().split()
    ko,en,ma = int(ko),int(en),int(ma)
    name_list.append([ko,en,ma,name])

ko_list=sorted(name_list, key=lambda x: (-x[0],x[1],-x[2],x[3]))
# lambda 안 쓰고 리스트에 모두 넣어서 count 정렬을 써보려했으나
# 시간초과.

for i in range(N):
    print(ko_list[i][3])