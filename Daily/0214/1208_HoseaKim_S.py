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

    for _ in range(n):
        i = 0
        j = h_len - 1
        min_h = h_list[i]
        max_h = h_list[j]
        while True:
            if min_h == h_list[i]:
                h_list[i] += 1
                i += 1
            else:
                i = 0
                min_h += 1
            if max_h == h_list[j]:
                h_list[j] -= 1
                j -= 1
            else:
                j = h_len - 1
                max_h -= 1

    return


T = 10
for case in range(1, T+1):
    n = int(input())
    h_list = list(map(int, input().split()))
    h_len = len(h_list)

    print(f'#{case}', flatten(sorting(h_len, h_list)))
