H,W = map(int,input().split())
block=list(map(int,input().split()))
stack = []
volume = 0

for i in range(W):
    while stack and block[i]>block[stack[-1]]:
        top = stack.pop()
        if not len(stack):
            break

        distance = i-stack[-1]-1
        waters=min(block[i],block[stack[-1]])-block[top]

        volume += distance * waters
    stack.append(i)
print(volume)