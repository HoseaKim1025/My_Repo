def bfs(n, arr, s):

    q = [[s[0], s[1]]]
    v = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        t = q.pop(0)
        for d in range(4):
            i, j = t[0]+dx[d], t[1]+dy[d]
            if 0 <= i < n and 0 <= j < n:
                if arr[i][j] == 0 and not v[i][j]:
                    q.append([i, j])
                    v[i][j] = v[t[0]][t[1]] + 1
                elif arr[i][j] == 3:
                    return v[t[0]][t[1]]

    return 0

def find_start(n, arr):

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return [i, j]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    start = find_start(n, arr)

    print(f'#{case}', bfs(n, arr, start))
