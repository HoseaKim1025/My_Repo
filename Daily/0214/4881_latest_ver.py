def arr_min_sum(i, n, s):
    global ans
    if s >= ans:
        return
    elif i == n:
        s = 0
        for j in range(n):
            s += arr[j][j]
        if ans > s:
            ans = s
    else:
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            arr_min_sum(i+1, n, s+arr[i][i])
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 1000000000
    arr_min_sum(0, n, 0)

    print(f'#{case}', ans)
