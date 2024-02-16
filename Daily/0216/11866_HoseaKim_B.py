# 요세푸스 문제 0

n, k = map(int, input().split())

top = -1
stack = list(range(1, n+1))
compare = [0] * n
ans = [0] * n
i = 0
while stack != compare:
    for _ in range(k):
        top = (top + 1) % n
        while stack[top] == 0:
            top = (top + 1) % n
    ans[i] = stack[top]
    i += 1
    stack[top] = 0

print(f'<{str(ans)[1:-1]}>')
