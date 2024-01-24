import sys

n, m = map(int, input().split())
data = [sys.stdin.readline().strip() for i in range(n+m)]
print(data)