# 최대 상금
def permutation(i, cnt, temp):
    global max_ss

    if temp and max_ss % (10**(num_len-i+1)) // (10**(num_len-i)) > temp:
        return
    if cnt == n:
        ss = 0
        for j in range(num_len):
            ss += num_list[p[j]] * 10**(num_len-1 - j)
        if max_ss < ss:
            max_ss = ss
        return
    else:
        for j in range(i+1, num_len):
            if p[i] == p[j]:
                continue
            p[i], p[j] = p[j], p[i]
            if i+1 < num_len:
                permutation(i, cnt+1, temp)
            p[i], p[j] = p[j], p[i]
        if i+1 < num_len:
            permutation(i+1, cnt, num_list[p[i]])


T = int(input())
for case in range(1, T+1):
    # 숫자판, 교환 횟수
    num, n = map(int, input().split())
    num_list = list(map(int, str(num)))

    num_len = len(num_list)
    p = list(range(num_len))
    max_ss = 0
    permutation(0, 0, 0)

    print(f'#{case}', max_ss)
