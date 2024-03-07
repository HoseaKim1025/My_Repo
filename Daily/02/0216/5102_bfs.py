'''
V E : V 1~V번 까지 v개의 정점. E 개의 간선
E개의 간선 정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, n, g):      # 시작정점 s, 노드개수 N
    q = []                  # 큐 생성
    visited = [0] * (n+1)   # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 인큐 표시
    while q:                # 처리안된 정점이 남아있으면
        t = q.pop(0)            # 처리할 정점 디큐
        if t == g:
            return visited[t]-1 # 최단 경로 간선 수
        for i in adjl[t]:      # t의 인접 정점이
            if visited[i] == 0:          # 인큐되지 않았으면
                q.append(i)
                visited[i] = visited[t]+1

    return 0    # G까지 경로가 없는 경우


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)     # 무향그래프
    print(adjl)
    S, G = map(int, input().split())
    # print(V, E, n1, n2, S, G)
    print(f'#{tc} {bfs(S, V, G)}')
