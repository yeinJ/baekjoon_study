dwarf=[int(input()) for _ in range(9)]
N = len(dwarf)
dwarf_list = []

for i in range(1<<N):
    a_list = []
    for j in range(N):
        if i & (1<<j):
            a_list.append(dwarf[j])
    if len(a_list) == 7:
        dwarf_list.append(a_list)

for i in dwarf_list:
    sum_num=0
    for j in range(7):
        sum_num += i[j]
    if sum_num == 100:
        real_dwarf = sorted(i)
        break

for i in real_dwarf:
    print(i)