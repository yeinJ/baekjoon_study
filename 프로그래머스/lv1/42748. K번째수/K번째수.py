def solution(array, commands):
    answer = []
    for i,j,k in commands:
        i,k= i-1,k-1
        arr=array[i:j]
        arr.sort()
        answer.append(arr[k])
        
    return answer