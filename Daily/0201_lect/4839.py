def binary_search(p, x):
    L = 1
    R = p
    cnt = 0

    while True:
        cnt += 1
        c = int((L + R) / 2)
        if x < c:
            R = c
        elif x > c:
            L = c
        else:
            return cnt


T = int(input())
for case in range(1, T+1):
    p, a, b, = map(int, input().split())

    A = binary_search(p, a)
    B = binary_search(p, b)
    # print(A, B)
    print(f'#{case}', end=' ')
    if A < B:
        print('A')
    elif A > B:
        print('B')
    else:
        print(0)
