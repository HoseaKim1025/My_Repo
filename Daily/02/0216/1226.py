# 미로1

from collections import deque


def bfs(dq):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while dq:
        t = dq.popleft()
        for d in range(4):
            i = t[0] + dx[d]
            j = t[1] + dy[d]
            if 0 <= i < 16 and 0 <= j < 16:
                if arr[i][j] == 0:
                    dq.append([i, j])
                    arr[i][j] = 4
                elif arr[i][j] == 3:
                    return 1

    return 0


def find_start(arr):

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return [i, j]


for _ in range(10):
    case = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    start = find_start(arr)

    print(f'#{case}', bfs(deque([start])))
