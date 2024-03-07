def continuous(n, seq):
    cnt = 0
    max_cnt = 0
    for i in range(n):
        if seq[i] == '1':
            cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
        if seq[i] == '0':
            cnt = 0

    return max_cnt


T = int(input())
for case in range(1, T+1):
    n = int(input())
    seq = input()

    print(f'#{case} {continuous(n, seq)}')
