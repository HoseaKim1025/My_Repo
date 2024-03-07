# Flatten

def sorting(h_len, h_list):

    cnt = [0] * 101
    for h in h_list:
        cnt[h] += 1

    for i in range(1, 101):
        cnt[i] += cnt[i-1]

    sorted_h_list = [0] * h_len
    for h in h_list:
        cnt[h] -= 1
        sorted_h_list[cnt[h]] = h

    return sorted_h_list


def flatten(sorted_h_list):

    i = 0
    j = h_len - 1
    min_h = sorted_h_list[i]
    max_h = sorted_h_list[j]
    cnt = 0
    while cnt < n:
        cnt += 1
        if min_h == sorted_h_list[i]:
            sorted_h_list[i] += 1
            i += 1
            if min_h != sorted_h_list[i]:
                i = 0
                min_h += 1
        if max_h == sorted_h_list[j]:
            sorted_h_list[j] -= 1
            j -= 1
            if max_h != sorted_h_list[j]:
                j = h_len - 1
                max_h -= 1

    return max_h - min_h


T = 10
for case in range(1, T+1):
    n = int(input())
    h_list = list(map(int, input().split()))
    h_len = len(h_list)

    print(f'#{case}', flatten(sorting(h_len, h_list)))
