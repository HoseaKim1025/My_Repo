def stack(n, num_list):

    top = -1
    st = [0] * n
    cnt = 0
    ans = ''
    i = 0
    while i < n:
        if st[top] < num_list[i]:
            top += 1        # push
            cnt += 1
            st[top] = cnt
            ans += '+'
        elif st[top] == num_list[i]:
            st[top] = 0     # pop
            top -= 1
            ans += '-'
            i += 1
        else:
            print('NO')
            return

    print(*ans, sep='\n')
    return


n = int(input())
num_list = [int(input()) for _ in range(n)]
stack(n, num_list)
