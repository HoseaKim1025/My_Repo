def palindrome(n, m, str_list):

    for i in range(n):
        # print(str_list[i])
        for j in range(n-m+1):
            ans_i = ['', '']
            ans_j = ['', '']
            cnt_i = 0
            cnt_j = 0
            for k in range(m//2):
                # print('i, j, k :', i, j, k)
                if str_list[i][j+k] == str_list[i][j+m-1-k]:
                    ans_i[0] += str_list[i][j+k]
                    ans_i[1] += str_list[i][j+m-1-k]
                    cnt_i += 1
                    # print('i', str_list[i][j+k], str_list[i][j+m-1-k], cnt_i)
                if str_list[j+k][i] == str_list[j+m-1-k][i]:
                    ans_j[0] += str_list[j+k][i]
                    ans_j[1] += str_list[j+m-1-k][i]
                    cnt_j += 1
                    # print('j', str_list[j+k][i], str_list[j+m-1-k][i], cnt_j)
            if cnt_i == m//2:
                if m % 2 == 0:
                    return ans_i[0] + ans_i[1][::-1]
                else:
                    return ans_i[0] + str_list[i][j+m//2] + ans_i[1][::-1]
            if cnt_j == m//2:
                if m % 2 == 0:
                    return ans_j[0] + ans_j[1][::-1]
                else:
                    return ans_j[0] + str_list[j+m//2][i] + ans_j[1][::-1]


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    str_list = [input() for _ in range(n)]

    print(f'#{case} {palindrome(n, m, str_list)}')
