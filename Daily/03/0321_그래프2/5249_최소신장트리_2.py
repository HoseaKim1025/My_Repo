# 3월 21일 <그래프2> 5249 최소 신장 트리 풀이2 kruskal
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    # 더 작은 루트노트에 합친가
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for case in range(1, T+1):
    V, E = map(int, input().split())    # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
    edge = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([u, v, w])
    edge.sort(key=lambda x : x[2])
    parents = [i for i in range(V+1)]       # 대표원소 배열
    print(edge)

    # MST의 간선수 N = 정점 수 - 1
    cnt = 0     # 선택한 edge의 수
    total = 0   # MST 가중치의 합
    for u, v, w in edge:
        # 다른 집합이라면
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == V:  # MST 구성이 끝나면
                break
    print(f'#{case}', total)