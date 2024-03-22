# 3월 19일 <병합정복, 백트래킹> 1865 동철이의 일 분배
def combination(i, ss):
    global max_p
    if i == n:
        if max_p < ss:
            max_p = ss
        return
    # if ss * min_v*(n-i) <= max_p:
    #     return
    # if ss < max_p:
    #     return
    if ss * max_v*(n-i) <= max_p:
        return
    for j in range(i, n):
        arr[i], arr[j] = arr[j], arr[i]
        if arr[i][i] != 0:
            combination(i+1, ss*arr[i][i]*0.01)
        # combination(i+1, ss*arr[i][i])
        arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # min_v = 100
    # for i in range(n):
    #     for j in range(n):
    #         if min_v > arr[i][j] != 0:
    #             min_v = arr[i][j]
    # min_v /= 100
    max_v = max(map(max, arr))
    max_p = 0
    combination(0, 1)

    # max_p = (max_p/(100**n))*100
    # print(f'#{case} {max_p:.6f}')
    print(f'#{case} {max_p*100:.6f}')
