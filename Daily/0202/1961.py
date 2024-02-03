def turn(n, arr):

    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[j][n-1-i] = str(arr[i][j])

    return new_arr


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_90 = turn(n, arr)
    arr_180 = turn(n, arr_90)
    arr_270 = turn(n, arr_180)

    print(f'#{case}')
    for i in range(n):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))