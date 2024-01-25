n = int(input())

def factorization(n):
    if n == 1:
        return
    for i in range(2, n+1):
        for _ in range(n+1):
            q = n % i
            if q != 0:
                break
            n //= i
            print(i)

factorization(n)