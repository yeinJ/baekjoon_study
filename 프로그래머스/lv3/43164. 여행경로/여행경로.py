'''
주어진 항공권을 모두 이용하여 여행경로 짜기
ICN에서 출발
방문한 공항 경로는 배열에 담아 Return
'''
def solution(tickets):
    answer = ['ICN']
    tickets.sort()
    n=len(tickets)
    visited=[0]*n
    tic_answer=[]
    def dfs(answer,visited):
        nonlocal tic_answer,n
        if sum(visited)==n and tic_answer==[]: 
            print(f'답 : {answer}')
            tic_answer.extend(answer)
            return

        for i in range(n):
            s,e = tickets[i]
            if s==answer[-1] and visited[i]==0:
                visited[i]=1
                answer.append(e)
                dfs(answer,visited)
                visited[i]=0
                answer.pop()
    dfs(answer,visited)
        
        
    return tic_answer