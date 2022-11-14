import sys
input = sys.stdin.readline
n = int(input())
number = [0]+list(map(int,input().split()))
tmp = [0]*(n+1)
cnt = 0
def merge_sort(s,e): # 병합정렬
    global cnt
    if e-s < 1 : # e보다 s가 크면 종료
        return
    m = int((s+e)/2) # s와 e 사이의 중간값 구하기
    merge_sort(s,m) # 분할한 구간에서 앞 부분 병합정렬
    merge_sort(m+1,e) # 분할한 구간에서 뒷 부분 병합정렬
    for i in range(s,e+1):
        tmp[i]=number[i]
    k = s
    index1 = s
    index2 = m+1
    while index1 <= m and index2<=e: # 각각의 수행조건(s<=m, m+1<=e)
        if tmp[index1]>tmp[index2]:
            cnt += m-index1+1
            number[k]=tmp[index2]
            k += 1
            index2+=1
        else :          # index1보다 index2가 클 경우, index1늘려주기
            number[k]=tmp[index1]
            k+=1
            index1+=1
    while index1 <= m:
        number[k]=tmp[index1]   # index1이 더 커서 남아있는 경우
        k+=1
        index1+=1
    while index2 <= e:
        number[k]=tmp[index2]   # index2가 값이 더 커서 남아있는 경우
        k+=1
        index2+=1

merge_sort(1,n)
print(cnt)