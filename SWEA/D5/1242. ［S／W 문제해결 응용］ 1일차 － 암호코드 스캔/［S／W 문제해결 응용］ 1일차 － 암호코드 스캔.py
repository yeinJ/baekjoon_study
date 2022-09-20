word = [[2,1,1],[2,2,1],[1,2,2],[4,1,1],[1,3,2],[2,3,1],[1,1,4],[3,1,2],[2,1,3],[1,1,2]]
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    word_list = []
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        k_list =[]
        for j in range(M):
            if arr[i][j]!='0' and arr[i-1][j]=='0':
                break
        word_list1 = []
        for h in range(j,M):
            if arr[i-1][h]!='0':
                continue
            else :
                word_list1.append(arr[i][h])
        word_list.append("".join(word_list1))

    for i in range(len(word_list)):
        if word_list[i]:
            word_list[i]=int(word_list[i],16)
            word_list[i]=format(word_list[i],'b')

    b_list = []
    ans = 0
    for i in range(len(word_list)):
        a_list = []
        cnt_one, cnt_zero = 0, 0
        for j in range(len(word_list[i])):
            if word_list[i][j] == '1':
                cnt_one += 1
                if cnt_zero != 0 and len(a_list)%3 !=0:
                    a_list.append(cnt_zero)
                    cnt_zero = 0
                elif len(a_list)%3 == 0:
                    cnt_zero = 0
            elif word_list[i][j]=='0':
                cnt_zero += 1
                if cnt_one != 0:
                    a_list.append(cnt_one)
                    cnt_one = 0
        password = []
        for j in range(len(a_list)//3):
            for h in range(len(word)):
                a,b,c=a_list[3*j],a_list[3*j+1],a_list[3*j+2]
                min_n = min(a,b,c)
                a1,b1,c1 = a//min_n,b//min_n,c//min_n
                if [a1,b1,c1]==word[h]:
                    password.append(h)

        hol,jjak =0,0
        for j in range(len(password)):
            if j==7 or j==15 :
                if (hol*3+jjak+password[j])%10==0:
                    b_list.append(hol+jjak+password[j])
                hol,jjak=0,0

            else :
                if j%2:
                    jjak += password[j]
                else :
                    hol += password[j]


    print(f'#{tc} {sum(b_list)}')
