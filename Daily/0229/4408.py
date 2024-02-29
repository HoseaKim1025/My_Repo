# 자기 방으로 돌아가기
T = int(input())
for case in range(1, T+1):
    n = int(input())
    # info = [list(map(int, input().split())) for _ in range(n)]
    '''
    info.sort(key=lambda x: x[0])
    max_time = 1
    for i in range(n):
        if info[i][0] % 2 == 0:
            info[i][0] -= 1
        if info[i][1] % 2 == 0:
            info[i][1] -= 1
        if info[i][0] > info[i][1]:
            info[i][0], info[i][1] = info[i][1], info[i][0]
    for i in range(n-1):
        L = info[i][0]
        R = info[i][1]
        time = 1
        for j in range(i+1, n):
            if L <= info[j][0] <= R or L <= info[j][1] <= R:
                time += 1
        if max_time < time:
            max_time = time
    '''
    corridor = [0] * 400
    max_v = 0

    for _ in range(n):
        start, end = map(int, input().split())

        if start % 2 == 0:
            start -= 1
        if end % 2 == 0:
            end -= 1
        if start > end:
            start, end = end, start

        for i in range(start, end+1):
            corridor[i] += 1
            max_v = max(corridor[i], max_v)

    print(f'#{case}', max_v)
