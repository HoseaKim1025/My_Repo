# 3월 21일 <그래프2> 5251 최소 이동 거리
import heapq


def dijkstra(start):
    pq = []
    # 시작 노드 최단 거리는 0
    # heapq 에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬된다.
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    # 우선순위 큐가 빌 때 까지 반복
    while pq:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            # 다음 노드를 가는 데 더 많은 비용이 드는 경우
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


INF = int(1e9)  # 무한을 의미하는 값으로 10억
T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    start = 0
    # 인접리스트 만들기
    graph = [[] for i in range(m)]
    # 누적거리를 저장할 테이블 - INF 로 저장
    distance = [INF] * (n+1)

    # 간선 정보를 입력
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])

    # 다익스트라 알고리즘 실행
    dijkstra(start)

    print(f'#{case}', distance[-1])
