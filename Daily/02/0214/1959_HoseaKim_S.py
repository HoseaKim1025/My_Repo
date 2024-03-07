# 두 개의 숫자열

def two_num_series(n, m, a_list, b_list):

    if n <= m:
        min_len = n
        min_list = a_list
        max_len = m
        max_list = b_list
    else:
        min_len = m
        min_list = b_list
        max_len = n
        max_list = a_list

    max_sum = -1000000000
    for i in range(max_len - min_len + 1):
        ss = 0
        for j in range(min_len):
            ss += max_list[i+j] * min_list[j]
        if max_sum < ss:
            max_sum = ss

    return max_sum


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    print(f'#{case}', two_num_series(n, m, a_list, b_list))
