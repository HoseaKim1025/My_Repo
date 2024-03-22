# 3월 20일 <그래프> 5247 연산
from collections import deque


def bfs():
    dq = deque()
    dq.append(n)
    cnt = 0
    visited = [0] * (10**6+1)
    while dq:
        cnt += 1
        dq_len = len(dq)
        for _ in range(dq_len):
            t = dq.popleft()
            for i in [t+1, t-1, t*2, t-10]:
                if i == m:
                    return cnt
                if 0 < i <= 10**6:
                    if not visited[i]:
                        dq.append(i)
                        visited[i] = 1


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())

    print(f'#{case}', bfs())
