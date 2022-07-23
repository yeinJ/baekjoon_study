N=int(input())
a=[]

if (N%5)==0 :
    a.append(N//5)
elif (N%3==0) and (N<15) :
    a.append(N//3)
elif ((N//5!=0) or (N//3!=0)) and (N<5):
    a.append(-1)
    
for i in range(N//5):
    if (((N%5)+(5*i))%3==0) and (N>5):
        a.append((N//5)-i+(((N%5)+(5*i))//3))
        break
    else :
        a.append(-1)
#print(a) # 값 확인용

if -1 in set(a) :
    if len(set(a)) >= 2:
        print(sorted(list(set(a)))[1])
        
    else :
        print(-1)
        
else :
    print(a[0])
        
