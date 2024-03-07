# 기차 사이의 파리
T = int(input())
for case in range(1, T+1):
    d, a, b, f = map(int, input().split())

    T = d * f / (a + b)

    print(f'#{case}', T)
