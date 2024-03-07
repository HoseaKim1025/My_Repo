def inorder_traversal(i):
    global cnt
    if i > e+1:
        return
    else:
        cnt += 1
        if L[i] != 0:
            inorder_traversal(L[i])
        if R[i] != 0:
            inorder_traversal(R[i])


T = int(input())
for case in range(1, T+1):
    e, n = map(int, input().split())
    num_list = list(map(int, input().split()))

    L = [0] * (e+2)
    R = [0] * (e+2)
    par = [0] * (e+2)
    for i in range(e):
        p, c = num_list[i*2], num_list[i*2+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        par[c] = p

    cnt = 0
    inorder_traversal(n)

    print(f'#{case}', cnt)
