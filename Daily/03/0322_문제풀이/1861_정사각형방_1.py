# 완전탐색 + 약간의 백트래킹 (10ms 감축..)
def f(x, y):
    cnt = 1
    while True:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] - arr[x][y] == 1:
                    x, y = nx, ny
                    cnt += 1
                    break
        else:
            break
    return cnt


T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 1
    ans = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            cnt = f(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                ans = arr[i][j]
            elif max_cnt == cnt and ans > arr[i][j]:
                ans = arr[i][j]

    print(f'#{case}', ans, max_cnt)
