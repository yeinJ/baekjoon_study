import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
targets = list(map(int,input().split()))
start = 0
end = N-1

def binary_sort(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid+1
        else :
            end = mid-1
    return 0

for target in targets:
    print(binary_sort(A,target,start,end))