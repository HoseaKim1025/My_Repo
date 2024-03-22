# 3월 19일 <병합정복, 백트래킹> 5209 최소생산비용
def combination(i):
    global ss, min_cost
    if ss + min_v * (n-i) >= min_cost:
        return
    if i == n:
        ss = 0
        for j in range(n):
            ss += arr[j][j]
        if min_cost > ss:
            min_cost = ss
        return
    for j in range(i, n):
        arr[i], arr[j] = arr[j], arr[i]
        ss += arr[i][i]
        combination(i+1)
        ss -= arr[i][i]
        arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_v = min(map(min, arr))
    ss = 0
    min_cost = 99 * 15
    combination(0)

    print(f'#{case}', min_cost)
