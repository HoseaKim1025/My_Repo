def toggle(n, m, arr):
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, m+1):
                if m % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0
                else:
                    if (i+j+2) % k == 0:
                        if arr[i][j] == 0:
                            arr[i][j] = 1
                        else:
                            arr[i][j] = 0
            if arr[i][j] == 1:
                ans += 1

    return ans


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case}', toggle(n, m, arr))
