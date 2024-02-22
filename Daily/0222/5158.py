from collections import deque

T = int(input())
for case in range(1, T+1):
    n, h = input().split()
    n = int(n)
    h = list(h)

    dec = 0
    for i in range(n):
        if h[i].isalpha():
            h[i] = ord(h[i]) - 55
        else:
            h[i] = int(h[i])
        dec += h[i] * 16**(n-1-i)

    b = deque()
    while dec > 1:
        dec, r = divmod(dec, 2)
        b.appendleft(r)
    b.appendleft(dec)
    extra = len(b) % 4
    if extra:
        for i in range(4 - extra):
            b.appendleft(0)

    print(f'#{case} ', *b, sep='')
