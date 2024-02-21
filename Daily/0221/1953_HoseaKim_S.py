# 탈주범 검거
def bfs(n, arr, s):

    q = [[s[0], s[1]]]
    v = [[0] * m for _ in range(n)]
    v[s[0]][s[1]] = 1
    ans = 1

    while q:
        t = q.pop(0)
        now = arr[t[0]][t[1]]
        if v[t[0]][t[1]] < L:
            for d in range(4):
                if now in tunnel_type[d]:
                    i, j = t[0] + dx[d], t[1] + dy[d]
                    if 0 <= i < n and 0 <= j < m:
                        if arr[i][j] in tunnel_type[d-2] and not v[i][j]:
                            q.append([i, j])
                            v[i][j] = v[t[0]][t[1]] + 1
                            ans += 1

    return ans


T = int(input())
for case in range(1, T+1):
    # n : 세로, m : 가로
    # r, c : 뚜껑 좌표
    # L : 시간
    n, m, r, c, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    start = [r, c]
    #     →  ↓  ←   ↑
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    tunnel_type = [[1, 3, 4, 5], [1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7]]

    print(f'#{case}', bfs(n, arr, start))
