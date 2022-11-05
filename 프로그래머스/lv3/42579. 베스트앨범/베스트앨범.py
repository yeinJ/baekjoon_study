'''
속한 노래가 많이 재생된 장르 먼저 수록
장르 내에 많이 재생된 노래 먼저 수록
재생횟수가 같으면 고유번호 낮은 노래 먼저 수록
i는 고유번호가 i인 노래 장르
'''
def solution(genres, plays):
    n = len(genres)
    answer=[]
    gen = list(set(genres))
    dic_gen = dict()
    for i in range(n):
        if genres[i] in dic_gen:
            dic_gen[genres[i]].append(plays[i])
        else :
            dic_gen[genres[i]]=[plays[i]]
        dic_gen[genres[i]].sort(reverse=True)
    sorted_dic = sorted(dic_gen.items(), key=lambda item:(sum(item[1]),item[1]),reverse=True)
    # for i in sorted_dic:
    #     i[1]
    for i in sorted_dic:
        cnt = 0
        for h in range(len(i[1])):
            for j in range(n):
                if i[1][h]==plays[j] and i[0]==genres[j]:
                    if j not in answer:
                        answer.append(j)
                        cnt +=1
                        break
                    else :
                        continue
                    
            if cnt == 2:
                break
    
    return answer