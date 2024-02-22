# 이진수2 (0.xxx~ 십진수를 이진수로 변환)

def bin(n):
    b = []
    v = []
    while n or n not in v:
        n = n * 2
        if n >= 1:
            n -= 1
            b.append(1)
        else:
            b.append(0)
        if len(b) >= 13:
            return 'overflow'
        v.append(n)
    return b


T = int(input())
for case in range(1, T+1):
    n = float(input())

    ans = bin(n)
    print(f'#{case} ', *ans, sep='')
