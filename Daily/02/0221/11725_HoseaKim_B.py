# 트리의 부모 찾기
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(i):
    for j in connect_dict[i]:
        if not par[j]:
            par[j] = i
            if len(connect_dict[j]) > 1:
                dfs(j)


N = int(input())

k = list(range(1, N+1))
v = [[] for _ in range(N)]
connect_dict = dict(zip(k, v))

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    connect_dict[node1].append(node2)
    connect_dict[node2].append(node1)

par = [0] * (N+1)
dfs(1)

print(*par[2:], sep='\n')
