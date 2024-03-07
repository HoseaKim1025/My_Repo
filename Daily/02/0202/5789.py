def box_change(n, q, LR_list):

    box_list = [0] * n
    for i in range(q):
        L = LR_list[i][0]
        R = LR_list[i][1]
        for j in range(L-1, R):
            box_list[j] = i+1

    return box_list


T = int(input())
for case in range(1, T+1):
    n, q = map(int, input().split())
    LR_list = [list(map(int, input().split())) for _ in range(q)]

    print(f'#{case}', *box_change(n, q, LR_list))