T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = round(N**(1/3))       # 3제곱근 구한다.(반올림해서 양의 정수로)
    if ans**3 != N:             # 구한값을 세제곱할때 값이 N과 같으면 ans 그대로
        ans = -1                # 아니면 -1
    print(f'#{tc} {ans}')