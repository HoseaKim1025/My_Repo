T = int(input())
for case in range(1, T+1):
    n = int(input())
    card = list(input().split())

    print(f'#{case}', end=' ')

    a = 0
    if n % 2 == 1:
        b = n // 2 + 1
    else:
        b = n // 2
    for i in range(n//2):
        print(card[a], card[b], end=' ')
        a += 1
        b += 1
    if n % 2 == 1:
        print(card[a], end='')

    print()
