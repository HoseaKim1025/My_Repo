import sys

n, m = map(int, input().split())
n_set = set(list(sys.stdin.readline().strip() for _ in range(n)))
m_list = list(sys.stdin.readline().strip() for _ in range(m))

count = 0
for n_each in n_set:
    count += m_list.count(n_each)

print(count)