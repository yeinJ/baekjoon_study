import collections

def solution(participant, completion):
#     answer=[]
#     list_par=list(set(participant))
#     list_num=[0 for _ in range(len(list_par))]
#     dict_par=dict(zip(list_par,list_num))
#     for i in participant:
#         dict_par[i]+=1
#     for i in completion:
#         dict_par[i]-=1
#     for key,value in dict_par.items():
#         if value!=0:
#             answer.append(key)
            
#     return ''.join(answer)

    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]