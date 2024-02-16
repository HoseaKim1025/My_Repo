def diet(i, ss, cal):
    global max_ss
    if max_ss < ss:
        max_ss = ss
    for j in range(i, n):
        i += 1
        if cal + info[p[j]][1] > L:
            break
        diet(i, ss + info[p[j]][0], cal + info[p[j]][1])


T = int(input())
for case in range(1, T+1):
    # n : 재료의 수, L : 제한 칼로리
    n, L = map(int, input().split())
    # [맛, 칼로리]
    info = [list(map(int, input().split())) for _ in range(n)]
    info.sort(key=lambda x: x[1])

    p = list(range(n))
    max_ss = 0
    diet(0, 0, 0)

    print(f'#{case}', max_ss)
