T = int(input())
for case in range(1, T+1):
    n, k = list(map(int, input().split()))
    a = list(range(1, 13))
    ans = 0
    for i in range(1, 1 << 12):
        cnt = 0
        s = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                s += a[j]
        if cnt == n and s == k:
            ans += 1

    print(f'#{case} {ans}')
