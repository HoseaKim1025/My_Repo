t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    sum_list = []

    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += a_list[i+j]
        sum_list.append(sum)
    sum_list.sort()
    print(sum_list)

    ans = sum_list[-1] - sum_list[0]
    print(f'#{case} {ans}')