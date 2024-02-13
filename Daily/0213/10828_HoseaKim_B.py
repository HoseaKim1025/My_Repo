def stack(n, command):

    top = -1
    st = [0] * n
    for i in range(n):
        if command[i][0] == 'push':
            top += 1    # append
            st[top] = command[i][1]
        elif command[i][0] == 'pop':
            if st[top] == 0:
                print(-1)
            else:
                print(st[top])
                st[top] = 0
                top -= 1
        elif command[i][0] == 'size':
            for j in range(n):
                if st[j] == 0:
                    print(j)
                    break
        elif command[i][0] == 'empty':
            if st[0] == 0:
                print(1)
            else:
                print(0)
        elif command[i][0] == 'top':
            if st[top] == 0:
                print(-1)
            else:
                print(st[top])

    return


n = int(input())
command = [list(map(str, input().split())) for _ in range(n)]

stack(n, command)
