for _ in range(10):
    case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # for i in range(100):
    #     print(f'{i} : {ladder[i]}')

    for i in range(100):
        if ladder[99][i] == 2:
            pos = [99, i]

    while pos[0] > 0:
        # print(pos)
        if 0 <= pos[1] - 1 and ladder[pos[0] - 1][pos[1] - 1] == 1:
            # print('left')
            # print(pos)
            pos[0] -= 1
            pos[1] -= 1
            # print(pos)
            while 0 <= pos[1] - 1 and ladder[pos[0]][pos[1] - 1] == 1:
                # print(pos)
                pos[1] -= 1
        elif pos[1] + 1 < 100 and ladder[pos[0] - 1][pos[1] + 1] == 1:
            # print('right')
            pos[0] -= 1
            pos[1] += 1
            # print(pos)
            while pos[1] + 1 < 100 and ladder[pos[0]][pos[1] + 1] == 1:
                pos[1] += 1
                # print(pos)
        else:
            pos[0] -= 1

    ans = pos[1]
    print(f'#{case} {ans}')
