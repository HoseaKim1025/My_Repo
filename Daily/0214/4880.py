def card_game(start, end):
    L = start
    R = end
    if end - start > 1:
        L = card_game(start, (start + end)//2)
        R = card_game((end + start)//2 + 1, end)
    elif end - start == 0:
        return start

    if num_list[L - 1] == 1:
        if num_list[R - 1] == 2:
            return R
        else:
            return L
    if num_list[L - 1] == 2:
        if num_list[R - 1] == 3:
            return R
        else:
            return L
    if num_list[L - 1] == 3:
        if num_list[R - 1] == 1:
            return R
        else:
            return L


T = int(input())
for case in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    index = list(range(n))
    victory = 0

    print(f'#{case}', card_game(1, n))
