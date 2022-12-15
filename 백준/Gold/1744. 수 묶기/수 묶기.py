from queue import PriorityQueue
n = int(input())
minus_pq = PriorityQueue()
plus_pq =PriorityQueue()
zero, one = 0,0
for _ in range(n):
    num = int(input())
    if num > 0:
        plus_pq.put(-num) # 높은수부터 정렬하기 위해 - 해준다.
    elif num == 0 :
        zero += 1
    else :
        minus_pq.put(num)

ans = 0
num1 = 0
num2 = 0
while plus_pq.qsize() > 0:
    if plus_pq.qsize() >1:
        num1 = plus_pq.get()
        num2 = plus_pq.get()
        if -(num1+num2)>(num1*num2):
            ans += -(num1+num2)
        else :
            ans += (num1*num2)
    else :
        num1 = plus_pq.get()
        ans += -num1

while minus_pq.qsize() > 0:
    if minus_pq.qsize()==1:
        if zero>0:
            num1=minus_pq.get()
            ans += 0
        else :
            num1 = minus_pq.get()
            ans += num1
    else :
        num1=minus_pq.get()
        num2=minus_pq.get()
        ans += (num1*num2)
print(ans)