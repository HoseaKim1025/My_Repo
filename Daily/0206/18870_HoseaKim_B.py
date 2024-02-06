import sys
input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))

x_set = sorted(list(set(x_list)))
x_set_len = len(x_set)
idx_list = list(range(x_set_len))
new_dict = dict(zip(x_set, idx_list))
for i in range(n):
    x_list[i] = new_dict[x_list[i]]

print(*x_list)
