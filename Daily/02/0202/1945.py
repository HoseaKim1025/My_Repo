def factorization(n):

    cnt = [0] * 5
    prime = [2, 3, 5, 7, 11]
    for i in range(len(prime)):

        while True:
            q, r = divmod(n, prime[i])
            if r != 0:
                break
            n = q
            cnt[i] += 1

    return cnt


T = int(input())
for case in range(1, T+1):
    n = int(input())

    print(f'#{case}', *factorization(n))