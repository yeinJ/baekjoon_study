def solution(numbers, target):
    
    def find_answer(sum_num,i):
        nonlocal count
        if sum_num == target and i == len(numbers):
            count +=1
            return
        elif i==len(numbers):
            return    
        else :
            k=numbers[i]
            find_answer(sum_num+k,i+1)
            find_answer(sum_num-k,i+1)

             
    count = 0
    find_answer(0,0)
    
    return count