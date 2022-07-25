a=0
b=[]

for i in range(9):
    i=int(input())
    b.append(i)
    if i > a :
        a = i

count = 0
for j in b :
    if j != a:
        count += 1
    else :
        count += 1
        break
                

print(a)
print(count)