# 카드2
from collections import deque

n = int(input())

c = deque(list(range(1, n+1)))
cnt = 0
while len(c) > 1:
    if cnt % 2 == 0:
        c.popleft()
    else:
        c.append(c.popleft())
    cnt += 1

print(c[0])
