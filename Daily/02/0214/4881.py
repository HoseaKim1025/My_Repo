def arr_min_sum(i, n):
    global ans
    if i == n:
        s = 0
        for j in range(n):
            s += arr[j][p[j]]
        if ans > s:
            ans = s
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            arr_min_sum(i+1, n)
            p[i], p[j] = p[j], p[i]
    return ans


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 1000000000
    p = list(range(n))

    print(f'#{case}', arr_min_sum(0, n))
