T = int(input())
for case in range(1, T+1):
    b = list(map(int, input()))

    dec = [0] * 10
    for i in range(10):
        for j in range(7):
            dec[i] += b[i*7 + j] * 2**(6-j)

    print(f'#{case}', *dec)
