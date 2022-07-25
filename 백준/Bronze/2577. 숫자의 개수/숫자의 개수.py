A = int(input())
B = int(input())
C = int(input())

result = A*B*C
a=[]

result1=list(str(result))
for h in range(10):
    count=0
    for j in result1:
        if str(h)==j:
            count+=1
    print(count) 