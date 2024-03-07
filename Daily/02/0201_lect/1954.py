def f(n):
    if n == 1:
        print(1)
        return

    n_len = n

    area = [[0] * n for _ in range(n)]
    cnt = 0
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    pos = [0, 0]

    while n > 1:
        for i in range(4):
            k = 0
            while k < n - 1:
                cnt += 1
                area[pos[0]][pos[1]] = cnt
                pos[0] += direction[i][0]
                pos[1] += direction[i][1]
                k += 1
        n -= 2
        pos[0] += 1
        pos[1] += 1

    if n_len % 2 == 1:
        area[n_len // 2][n_len // 2] = cnt + 1

    for i in range(n_len):
        print(*area[i])
    return


T = int(input())
for case in range(1, T+1):
    n = int(input())

    print(f'#{case}')
    f(n)
