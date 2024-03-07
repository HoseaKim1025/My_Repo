T = int(input())
for case in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    for i in range(n-1):
        min_idx = i
        max_idx = i
        if i % 2 == 1:
            for j in range(i+1, n):
                if num_list[min_idx] > num_list[j]:
                    min_idx = j
            num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]
        else:
            for j in range(i+1, n):
                if num_list[max_idx] < num_list[j]:
                    max_idx = j
            num_list[max_idx], num_list[i] = num_list[i], num_list[max_idx]

    print(f'#{case}', *num_list[:10])
