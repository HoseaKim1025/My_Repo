# 3월 21일 <그래프2> 5250 최소비용
from heapq import heappop, heappush


def dijkstra():
    pq = []
    heappush(pq, (0, 0))
    distance[0] = 0
    while pq:
        now_cost, now_node = heappop(pq)
        if distance[now_node] >= now_cost:
            for next_cost, next_node in graph[now_node]:
                new_cost = now_cost + next_cost
                if distance[next_node] > new_cost:
                    distance[next_node] = next_cost
                    heappush(pq, (new_cost, next_node))


T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    # make graph
    graph = [[] for _ in range(N**2)]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    cost = arr[ni][nj] - arr[i][j]
                    if cost < 0:
                        cost = 0
                    now_node = i*3 + j
                    next_node = ni*3 + nj
                    graph[now_node].append([cost+1, next_node])

    distance = [1000] * N ** 2
    dijkstra()

    print(f'#{case}', distance[-1])
