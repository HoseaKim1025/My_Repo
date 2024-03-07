def balloon(n, m, arr):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_total = 0

    for i in range(n):
        for j in range(m):
            total = arr[i][j]
            for a in range(1, total+1):
                for d in range(4):
                    if 0 <= i+dx[d]*a < n and 0 <= j+dy[d]*a < m:
                        total += arr[i+dx[d]*a][j+dy[d]*a]
            if max_total < total:
                max_total = total

    return  max_total


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case} {balloon(n, m, arr)}')
