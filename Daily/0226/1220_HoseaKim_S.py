# Magnetic
from pprint import pprint


def f(i, j):
    if j == n:
        pass
    else:
        while mag_list[i][j]:
            t, mag_list[i][j] = mag_list[i][j], 0
            j += t
            if 0 <= j < n:
                mag_list[i][j] = t


T = 1
for case in range(1, T+1):
    n = int(input())    # = 100
    # 1 : n극 ↓, 2 : s극 ↑
    arr = [list(map(int, input().split())) for _ in range(n)]

    mag_list = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            # 1 : n극 ↓, -1 : s극 ↑
            if arr[i][j] == 1:
                mag_list[i][j] = 1
            if arr[i][j] == 2:
                mag_list[i][j] = -1
    pprint(mag_list)

    for i in range(n):
        for j in range(n):
            t, mag_list[i][j] = mag_list[i][j], 0
            j += t
            if 0 <= j < n:
                mag_list[i][j] = t

    f(0, 0)

    print(f'#{case}', )
