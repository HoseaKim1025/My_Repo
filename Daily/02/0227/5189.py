# 전자카트
def permutation(i, ss):
    global min_ss
    if min_ss <= ss:
        return
    if i == n:
        ss += arr[p[i-1]][p[i]]
        if min_ss > ss:
            min_ss = ss
        return
    for j in range(i, n):
        p[i], p[j] = p[j], p[i]
        permutation(i+1, ss+arr[p[i-1]][p[i]])
        p[i], p[j] = p[j], p[i]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    p = list(range(n))
    p.append(0)
    min_ss = 10**9
    permutation(1, 0)

    print(f'#{case}', min_ss)
