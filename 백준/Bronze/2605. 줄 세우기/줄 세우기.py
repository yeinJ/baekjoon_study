# 줄 세우기
N = int(input())
stack = []
lst = []
stu=list(map(int,input().split()))
for i in range(N):
    if stu[i] == 0:
        stack.append(i+1)
    else :
        for j in range(stu[i]):
            lst.append(stack.pop())
        stack.append(i+1)
        while lst:
            stack.append(lst.pop())

print(*stack)