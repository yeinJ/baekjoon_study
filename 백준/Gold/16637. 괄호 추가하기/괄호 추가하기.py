def operator(ope):
    if ope[1]=='+':
        numb = int(ope[0])+int(ope[2])
    elif ope[1]=='-':
        numb = int(ope[0])-int(ope[2])
    elif ope[1]=='*':
        numb = int(ope[0])*int(ope[2])

    return list([str(numb)])

def find_num(number1,k):
    global max_num
    u = 0
    number = number1[:]
    while len(number)>2:
        if str(abs(int(number[u]))).isdigit():
            number = operator(number[u:u+3])+number[u+3:]
    max_num = max(max_num,int(''.join(number)))
    if k+3>len(number1):
        return
    elif number1[k].isdigit():
        if k+3 == len(number):
            h = number1[:k] + operator(number1[k:k + 3])
        else :
            h=number1[:k]+operator(number1[k:k+3])+number1[k+3:]

        find_num(h,k+2)
        find_num(number1,k+2)


N = int(input())
max_num = -(2**31)
number1 = list(input()) # 숫자값은 항상 짝수 0,2,4
find_num(number1,0)
print(max_num)
