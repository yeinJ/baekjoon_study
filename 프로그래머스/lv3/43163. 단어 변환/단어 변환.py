# from collections import Counter
# def solution(begin, target, words):
#     visited=[0]*len(words)
#     answer = -1
#     def dfs(word,target,visited):
#         nonlocal answer
#         if answer:
#             answer=min(sum(visited),answer)
#         if sum(visited)==len(words) and word!=target:
#             answer = 0
#             return
#         if word == target:
#             answer=sum(visited)
#         else :
#             for h in range(len(words)):
#                 m = Counter(word)
#                 for w in words[h]:
#                     m[w]-=1
#                 cnt_1 = 0
#                 for value in m.values():
#                     if value == 1:
#                         cnt_1 +=1
#                     if cnt_1 >1 :
#                         break
#                 if cnt_1 == 1 and visited[h]==0:
#                     visited[h]=1
#                     dfs(words[h],target,visited)
#                     visited[h]=0
                    
#     if target not in words:
#         answer = 0
#         return answer
#     else :
#         dfs(begin,target,visited)
#         return answer

def solution(begin, target, words):
    if target not in words:
        return 0

    res = [float("inf")]

    def dfs(s, w_list, d, visited):
        if s == target:
            res[0] = min(res[0], d)
            return

        for i in w_list:
            unmatch = 0
            for a, b in zip(s, i):
                if a != b:
                    unmatch += 1
            if unmatch == 1 and (i not in visited):
                t = d + 1
                visited.add(i)
                dfs(i, w_list, t, visited)
                visited.remove(i) 

    dfs(begin, words, 0, set())

    return res[0]