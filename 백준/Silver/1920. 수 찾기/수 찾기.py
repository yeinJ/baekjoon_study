import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int,input().split()))
num_lst.sort()
m = int(input())
find_lst = list(map(int,input().split()))

def binary_sort(target,data):
    start = 0
    end = n-1
    while start <= end :
        mid = (start+end)//2
        if data[mid]==target:
            return True
        elif data[mid]<target:
            start=mid+1
        else :
            end=mid-1
    return False

for i in find_lst:
    if binary_sort(i,num_lst):
        print(1)
    else :
        print(0)