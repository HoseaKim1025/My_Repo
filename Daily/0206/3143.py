def fastest(a, b):
    a_len = len(a)
    b_len = len(b)
    ans = a_len
    i = 0
    while i <= a_len - b_len:
        cnt = 0
        for j in range(b_len):
            if a[i+j] == b[j]:
                cnt += 1
        if cnt == b_len:
            ans = ans - cnt + 1
            i += cnt
        else:
            i += 1
    return ans


T = int(input())
for case in range(1, T+1):
    a, b = map(str, input().split())

    print(f'#{case} {fastest(a, b)}')
