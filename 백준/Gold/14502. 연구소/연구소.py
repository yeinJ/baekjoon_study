import itertools
from collections import deque
import copy


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 2의 개수는 2보다 크거나 같고 10보다 작은 자연수
# 벽의 개수는 3개 , 꼭 3개를 세워야함
# 벽을 세우는 경우의 수
num_list = []

arr2 = copy.deepcopy(arr)                           # arr을 경우마다 바꿔줘야 하므로 deepcopy사용
di = [0,1,0,-1]
dj = [1,0,-1,0]
queue = deque()
max_zero = 0        # 0의 값이 최대가 될 때의 값 구하기
zero_num = -3       # 벽 3개가 세워지므로 0 위치에 벽이 무조건 3개는 들어간다고 가정
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            queue.append([i,j])
        if arr[i][j]==0:
            zero_num += 1
            num_list.append([i,j])
wall=list(itertools.combinations(num_list,3))       # num_list의 경우 조합으로 3개씩 뽑아내기
queue2 = copy.deepcopy(queue)
for h in wall:
    for si,sj in h:
        arr2[si][sj]=1
    change_cnt = 0
    while queue:
        i,j=queue.popleft()
        for h in range(4):
            ni = i + di[h]
            nj = j + dj[h]
            if 0<=ni<N and 0<=nj<M and arr2[ni][nj]==0:
                queue.append([ni,nj])
                arr2[ni][nj]=2
                change_cnt += 1     # 0에서 바뀌는 경우를 세준다.
        if zero_num-change_cnt < max_zero:
            break
    if zero_num-change_cnt > max_zero:
        max_zero = zero_num-change_cnt

    arr2 = copy.deepcopy(arr)       # 변화한 arr2는 초기화 시켜준다.
    queue= copy.deepcopy(queue2)
print(max_zero)