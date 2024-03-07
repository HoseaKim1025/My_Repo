def sum_tree(last):
    if info_list[last-1][1] in '*/+-':
       sum_tree(int(info_list[last-1][2]))
       sum_tree(int(info_list[last-1][3]))
       if info_list[last-1][1] == '*':
           info_list[last-1][1] = info_list[int(info_list[last-1][2])-1][1] * info_list[int(info_list[last-1][3])-1][1]
       elif info_list[last-1][1] == '/':
           info_list[last-1][1] = info_list[int(info_list[last-1][2])-1][1] // info_list[int(info_list[last-1][3])-1][1]
       elif info_list[last-1][1] == '+':
           info_list[last-1][1] = info_list[int(info_list[last-1][2])-1][1] + info_list[int(info_list[last-1][3])-1][1]
       elif info_list[last-1][1] == '-':
           info_list[last-1][1] = info_list[int(info_list[last-1][2])-1][1] - info_list[int(info_list[last-1][3])-1][1]
    else:
        info_list[last-1][1] = int(info_list[last-1][1])


for case in range(1, 11):
    N = int(input())
    info_list = [list(input().split()) for _ in range(N)]

    sum_tree(1)

    print(f'#{case}', info_list[0][1])
