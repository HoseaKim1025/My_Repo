t = int(input())
for case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    ans = a[-1] - a[0]

    print(f'#{case} {ans}')
