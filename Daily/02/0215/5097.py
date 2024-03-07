from collections import deque


def turn(n, m, num_list):

    dq = deque(num_list)
    for _ in range(m):
        L = dq.popleft()
        dq.append(L)

    return dq[0]


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    print(f'#{case}', turn(n, m, num_list))
