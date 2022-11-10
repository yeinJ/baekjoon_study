def solution(k, dungeons):
    max_num = 0
    n = len(dungeons)
    power=[0]*n
    
    def go_dungeon(k,power):
        nonlocal max_num
        if sum(power)>max_num:
            max_num=sum(power)
        cnt = 0
        for i in range(n):
            mi,de=dungeons[i]
            if k>=mi and power[i]==0:
                power[i]=1
                go_dungeon(k-de,power)
                power[i]=0
            elif k < mi:
                cnt +=1
        if cnt == n:
            return
                
            
    go_dungeon(k,power)
    
    return max_num