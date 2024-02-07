def find_rect(n, arr):
    max_mul = 0
    for i in range(n):
        for j in range(n):
            cnt_i = 0
            cnt_j = 1
            while j+cnt_i < n and arr[i][j+cnt_i] == 1:
                arr[i][j + cnt_i] = 0
                cnt_i += 1
                # print('cnt_i :', cnt_i)
            while i+cnt_j < n and arr[i+cnt_j][j] == 1:
                for x in range(cnt_i):
                    arr[i + cnt_j][j + x] = 0
                cnt_j += 1
                # print('cnt_j :', cnt_j)
            if max_mul < cnt_i * cnt_j:
                max_mul = cnt_i * cnt_j
    # print(arr)
    return max_mul


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case}', find_rect(n, arr))
