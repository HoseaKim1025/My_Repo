def find_parents(x):
    if parents[x] == x:
        return x

    return find_parents(parents[x])


def union(x, y):
    x = find_parents(x)
    y = find_parents(y)

    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    parents = list(range(N+1))
    for _ in range(M):
        s, e = map(int, input().split())
        union(s, e)

    ans = 0
    for i in range(1, N+1):
        if parents[i] == i:
            ans += 1

    print(f'#{case}', ans)
