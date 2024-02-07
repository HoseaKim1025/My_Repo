def password(n, num_str):
    stack = [''] * n
    top = -1
    for i in range(n):
        if stack[top] != num_str[i]:
            top += 1
            stack[top] = num_str[i]
        else:
            stack[top] = ''
            top -= 1

    return ''.join(stack)


for case in range(1, 11):
    n, num_str = input().split()
    n = int(n)
    print(f'#{case}', password(n, num_str))