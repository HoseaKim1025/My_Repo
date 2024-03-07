n = int(input())
info_list = [input().split() for _ in range(n)]
for i in range(n):
    info_list[i][0] = int(info_list[i][0])
idx_list = list(range(n))
new_list = list(zip(idx_list, info_list))
new_list.sort(key=lambda x: (x[1][0], x[0]))

for i in range(n):
    print(*new_list[i][1])
