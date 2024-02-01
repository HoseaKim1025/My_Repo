T = int(input())
for case in range(1, T+1):
    # n*n 파리, m*m 파리채
    n, m = map(int, input().split())
    pari_list = [list(map(int, input().split())) for _ in range(n)]

    arr = [[0]*(n-m+1) for _ in range(n-m+1)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            for x in range(m):
                for y in range(m):
                    arr[i][j] += pari_list[i+x][j+y]
    max_area = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            if max_area < arr[i][j]:
                max_area = arr[i][j]
    print(f'#{case} {max_area}')
