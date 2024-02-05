def arr_mul(n, m, k, arr1, arr2):
    result = [[0] * k for _ in range(n) ]
    for i in range(n):
        for j in range(k):
            # print(f'({i}, {j})')
            for a in range(m):
                result[i][j] += arr1[i][a] * arr2[a][j]
                # print(f'{arr}')

    return result


n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(m)]

ans = arr_mul(n, m, k, arr1, arr2)
for i in range(n):
    print(*ans[i])
