# 오목 판정
def f():
    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for d in range(4):
                    cnt = 1
                    for k in range(1, 5):
                        ni = i + dx[d] * k
                        nj = j + dy[d] * k
                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == 'o':
                                cnt += 1
                            else:
                                break
                        if cnt == 5:
                            return 'YES'
    return 'NO'


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    print(f'#{case}', f())
