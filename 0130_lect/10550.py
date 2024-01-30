def baby_gin(num_list):

    counts = [0] * 12
    for num in num_list:
        counts[num] += 1

    tri = run_cnt = 0
    i = 0
    while i <= 9:
        if counts[i] >= 3:
            counts[i] -= 3
            tri += 1
            continue
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run_cnt += 1
            continue
        i += 1
    if run_cnt + tri == 2:
        return 'Baby Gin'
    else:
        return 'Lose'


T = int(input())
for case in range(1, T+1):
    num_list = list(map(int, input()))

    print(f'#{case} {baby_gin(num_list)}')
