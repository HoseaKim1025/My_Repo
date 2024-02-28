# 입국심사 swea 3074
def f():
    global times
    R = n - 1
    L = -1
    pre = 0
    while True:
        while R != L:
            L += 1
            q = t[R] // t[L]
            times[L] += q
            if sum(times) < m:
                pass
            elif sum(times) == m:
                return
            elif sum(times) > m:
                times = [0] * n
                pre = R
                R -= 1
                L = -1


T = int(input())
for case in range(1, T+1):
    # n개의 심사대, m명의 입국심사
    n, m = map(int, input().split())
    # 심사대 별 심사 소요 시간
    t = [int(input()) for _ in range(n)]

    t.sort()
    times = [0] * n     # 각 검색대 몇 번 했는지
    f()

    ss = 0
    for i in range(n):
        ss += t[i] * times[i]

    print(f'#{case}', ss)
