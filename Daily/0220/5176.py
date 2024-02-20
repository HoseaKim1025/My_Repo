def inorder_traversal(i):
    global cnt
    if i > n:
        return
    else:
        inorder_traversal(i*2)
        cnt += 1
        a[i] = cnt
        inorder_traversal(i*2+1)


T = int(input())
for case in range(1, T+1):
    n = int(input())

    a = [0] * (n+1)
    cnt = 0
    inorder_traversal(1)

    print(f'#{case}', a[1], a[n//2])
