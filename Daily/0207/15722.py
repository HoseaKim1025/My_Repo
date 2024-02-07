def area_div(n, arr):
    min_diff = 36100
    for x in range(1, n):
        for y in range(1, n):
            sum_list = [0] * 4
            for i in range(x):
                for j in range(y):
                    sum_list[0] += arr[i][j]
            for i in range(x):
                for j in range(y, n):
                    sum_list[1] += arr[i][j]
            for i in range(x, n):
                for j in range(y):
                    sum_list[2] += arr[i][j]
            for i in range(x, n):
                for j in range(y, n):
                    sum_list[3] += arr[i][j]
            max_sum = sum_list[0]
            min_sum = sum_list[0]
            for area in sum_list:
                if max_sum < area:
                    max_sum = area
                if min_sum > area:
                    min_sum = area
            if min_diff > max_sum - min_sum:
                min_diff = max_sum - min_sum

    return min_diff


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case}', area_div(n, arr))
