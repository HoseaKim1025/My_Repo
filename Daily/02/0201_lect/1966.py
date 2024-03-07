def sel_sort(n, num_list):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]
    ans = list(map(str, num_list))
    return ' '.join(ans)


T = int(input())
for case in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    print(f'#{case} {sel_sort(n, num_list)}')
