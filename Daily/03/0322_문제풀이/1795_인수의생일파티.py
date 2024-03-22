from heapq import heappop, heappush


def dijkstra():
    return


T = int(input())
for case in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(M+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([-c, y])
    distance = [10**9] * (M+1)
    

    print(f'#{case}', )
