def solution(clothes):
    n = len(clothes)
    answer = 0
    comb = dict()
    for name, category in clothes:
        if category in comb:
            comb[category]+=1
        else :
            comb[category]=1
    answer = 1
    for num in comb.values():
        answer*=(num+1)
    answer -=1
        
    return answer