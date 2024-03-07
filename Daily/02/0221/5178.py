# 노드의 합

T = int(input())
for case in range(1, T+1):
    # 노드 개수, 리프 노드 개수, 출력 노드
    N, M, L = map(int, input().split())
    leaf_list = [tuple(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N+1)
    for node, key in leaf_list:
        tree[node] = key

    last = N
    while last > 1:
        tree[last//2] += tree[last]
        last -= 1

    print(f'#{case}', tree[L])
