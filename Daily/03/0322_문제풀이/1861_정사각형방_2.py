# DP + 약간의 백트래킹
T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    near = [0] * (N**2+1)
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] - arr[i][j] == 1:
                        near[arr[i][j]] = 1

    cnt = 0
    max_cnt = 0
    ans = 0
    for i in range(N**2, -1, -1):
        if cnt == 0 and max_cnt > i:
            break
        if near[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                ans = i
            cnt = 0

    print(f'#{case}', ans+1, max_cnt+1)
