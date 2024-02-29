# 재밌는 오셀로 게임
T = int(input())
for case in range(1, T+1):
    # 한 변의 길이, 돌 놓는 횟수
    n, m = map(int, input().split())
    # 돌의 좌표 i, j 와 색상 color (1흑 2백)
    arr = [[0] * n for _ in range(n)]
    arr[n//2-1][n//2-1] = arr[n//2][n//2] = 2
    arr[n//2][n//2-1] = arr[n//2-1][n//2] = 1
    d_list = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for _ in range(m):
        j, i, color = map(int, input().split())
        arr[i-1][j-1] = color
        if color == 1:
            temp = 2
        else:
            temp = 1
        for d in d_list:
            ni = i-1 + d[0]
            nj = j-1 + d[1]
            while 0 <= ni < n and 0 <= nj < n and arr[ni][nj]:
                if arr[ni][nj] == color:
                    ni -= d[0]
                    nj -= d[1]
                    while ni != i-1 or nj != j-1:
                        arr[ni][nj] = color
                        ni -= d[0]
                        nj -= d[1]
                    break
                ni += d[0]
                nj += d[1]
    black = 0
    white = 0
    for i in range(n):
        black += arr[i].count(1)
        white += arr[i].count(2)

    print(f'#{case}', black, white)
