# 10개 중 5개만 맞음
# def grouping(n, m, arr):
#     cnt = 0
#     if arr:
#         group = set(arr[0])
#         arr.pop(0)
#         cnt += 1
#         while group:
#             flag = 0
#             while flag == 0:
#                 flag = 1
#                 new_arr = arr[:]
#                 index = -1
#                 for i in range(len(arr)):
#                     index += 1
#                     for j in range(2):
#                         if arr[i][j] in group:
#                             group.update(set(arr[i]))
#                             new_arr.pop(index)
#                             index -= 1
#                             flag = 0
#                             break
#                 arr = new_arr
#
#             if arr:
#                 group = set(arr[0])
#                 arr.pop(0)
#                 cnt += 1
#             else:
#                 group = set()
#     return cnt

# 10개 중 5개 맞춤
def grouping(n, m, arr):
    if n == 1 or m == 0:
        return len(arr)
    group = [set(arr[0])]
    k = 0
    for i in range(1, m):
        for j in range(2):
            if arr[i][j] in group[k]:
                group[k].update(arr[i])
                break
        else:
            group.append(set(arr[i]))
            k += 1
    g_len = len(group)
    i = 0
    while i < g_len-1:
        for j in range(i+1, len(group)):
            if group[i] & group[j]:
                group[i] |= group[j]
                group.remove(group[j])
                i = 0
                break
        else:
            i += 1

    return len(group)


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]

    print(f'#{case}', grouping(n, m, arr))
