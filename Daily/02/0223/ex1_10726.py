T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n):
        if m & (1 << i):
            cnt += 1

    if cnt == n:
        print(f'#{case} ON')
    else:
        print(f'#{case} OFF')
