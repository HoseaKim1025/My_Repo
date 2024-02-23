# 암호코드 스캔


def find_code():
    for i in range(n):
        for j in range(m):
            if arr[i][j] != '0':
                return [i, j]


def make_new_arr():
    start = find_code()
    i, j = start
    while arr[start[0]][j] != '0':
        arr[start[0]][j] = 0
        j += 1
    while arr[i][start[1]] != '0':
        arr[i][start[1]] = 0
        i += 1
    return i - start[0], j - start[1]


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    print(arr)

    w, h = make_new_arr()
    print(w, h)

    print(f'#{case}', )
