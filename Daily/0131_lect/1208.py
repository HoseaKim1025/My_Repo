T = 10
for case in range(1, T+1):
    total_dump = int(input())
    h_list = list(map(int, input().split()))

    # 카운트 정렬
    counts = [0] * 101
    for h in h_list:
        counts[h] += 1

    for i in range(1, 101):
        counts[i] += counts[i-1]

    sorted_h = [0] * len(h_list)
    for h in h_list:
        counts[h] -= 1
        sorted_h[counts[h]] = h

    # 덤프 실행
    dump = 0
    i = 0
    j = 0
    max_num = 100
    min_num = 1
    flag = 0
    while dump < total_dump:

        if flag == 0:
            if sorted_h[i] == min_num:
                sorted_h[i] += 1
            else:
                min_num += 1
                i = 0
                continue

        if sorted_h[len(sorted_h)-1-j] == max_num:
            sorted_h[len(sorted_h)-1-j] -= 1
        else:
            max_num -= 1
            j = 0
            flag = 1
            continue

        flag = 0
        i += 1
        j += 1
        dump += 1

    # 마지막 dump에서 min이나 max가 바뀌었다면 +1 또는 -1
    is_complete_min = 1
    is_complete_max = 1
    for x in range(len(sorted_h)):
        if sorted_h[x] == min_num:
            is_complete_min = 0
        if sorted_h[len(sorted_h)-1-x] == max_num:
            is_complete_max = 0

    if is_complete_min == 1:
        min_num += 1
    if is_complete_max == 1:
        max_num -= 1

    print(f'#{case} {max_num - min_num}')
