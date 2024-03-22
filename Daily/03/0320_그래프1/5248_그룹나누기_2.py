# 3월 20일 <그래프> 5248 그룹 나누기 풀이2 disjoint-set (서로소 집합)
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return find_set(parents[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    parents = list(range(n + 1))
    for i in range(m):
        union(arr[i * 2], arr[i * 2 + 1])

    cnt = 0
    for i in range(1, n + 1):
        if i == parents[i]:
            cnt += 1

    print(f'#{case} {cnt}')
