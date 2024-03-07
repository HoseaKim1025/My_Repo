def palindrome(pal_len, arr):

    ans = 0
    for i in range(8):
        for j in range(8-pal_len+1):
            cnt_i = 0
            cnt_j = 0
            for k in range(pal_len):
                if arr[i][j+k] == arr[i][j+pal_len-1-k]:
                    cnt_i += 1
                if arr[j+k][i] == arr[j+pal_len-1-k][i]:
                    cnt_j += 1
            if cnt_i == pal_len:
                ans += 1
            if cnt_j == pal_len:
                ans += 1

    return ans


for case in range(1, 11):
    pal_len = int(input())
    arr = [input() for _ in range(8)]

    print(f'#{case} {palindrome(pal_len, arr)}')
