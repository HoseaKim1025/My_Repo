def carrot(n, c_list):
    min_diff = n
    for i in range(1, n-1):
        for j in range(i+1, n):
            if (
                i > n//2 or j-i > n//2 or n-j > n//2 or
                c_list[i-1] == c_list[i] or c_list[j-1] == c_list[j]
            ):
                continue
            box = [i, j-i, n-j]
            max_box = 0
            min_box = n
            for x in box:
                if max_box < x:
                    max_box = x
                if min_box > x:
                    min_box = x
            if min_diff > max_box - min_box:
                min_diff = max_box - min_box

    if min_diff == n:
        return -1
    else:
        return min_diff


T = int(input())
for case in range(1, T+1):
    n = int(input())    # 당근의 개수
    c_list = list(map(int, input().split()))    # 당근 크기
    c_list.sort()
    print(f'#{case} {carrot(n, c_list)}')
