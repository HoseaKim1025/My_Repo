def inorder_traversal(i):
    if i < n:
        if len(in_list[i]) > 2:
            inorder_traversal(int(in_list[i][2])-1)
        print(in_list[i][1], end='')
        if len(in_list[i]) > 3:
            inorder_traversal(int(in_list[i][3])-1)


for case in range(1, 11):
    n = int(input())
    in_list = [list(input().split()) for _ in range(n)]

    print(f'#{case} ', end='')
    inorder_traversal(0)
    print()
