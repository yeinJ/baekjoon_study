'''
점수 중 최댓값 구하기
점수/M*100으로 고침
'''

N = int(input())
score = list(map(int,input().split()))    # 세준이점수
M=max(score)
for i in range(N):
    score[i]=score[i]/M*100

answer=sum(score)/N
print(answer)