from collections import deque
def solution(n, computers):
    visited = [0]*n
    answer = 0
    def dfs(i):
        nonlocal visited
        network = deque()
        network.append(i)
        visited[i]=1
        while network:
            si=network.popleft()
            for j in range(n):
                if (computers[si][j]==1 or computers[j][si]==1) and si!=j and visited[j]==0:
                    visited[j]=1
                    network.append(j)
                    
    for i in range(n):
        if visited[i]!=1:
            dfs(i)
            answer +=1
            
    return answer