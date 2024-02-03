def pari(n, m, arr):
    max_total = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for x in range(m):
                for y in range(m):
                    total += arr[i+x][j+y]
            if max_total < total:
                max_total = total

    return max_total


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case} {pari(n, m, arr)}')