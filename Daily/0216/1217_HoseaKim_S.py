# 거듭 제곱
def f(power):

    if power == m:
        return n

    return n * f(power+1)


for _ in range(10):
    case = input()
    n, m = map(int, input().split())

    print(f'#{case}', f(1))
