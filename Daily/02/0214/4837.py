def frac_set_sum(i, n, k, s, cnt):

    global ans
    if cnt == n and s == k:
        ans += 1
    elif s > k or i == 12:
        return
    else:
        frac_set_sum(i+1, n, k, s+a[i], cnt+1)
        frac_set_sum(i+1, n, k, s, cnt)


T = int(input())
for case in range(1, T+1):
    n, k = map(int, input().split())
    a = list(range(1, 13))
    ans = 0
    frac_set_sum(0, n, k, 0, 0)

    print(f'#{case}', ans)
