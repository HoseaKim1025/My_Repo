def forth(fx):

    top = -1
    fx_len = len(fx)
    stack = [False] * fx_len
    for i in range(fx_len):
        if fx[i] == '.':
            if top == 0:
                return stack[0]
            else:
                return 'error'
        elif fx[i] in '*/+-':
            if stack[top-1] and stack[top]:
                if fx[i] == '*':
                    stack[top-1] *= stack[top]
                elif fx[i] == '/':
                    stack[top-1] //= stack[top]
                elif fx[i] == '+':
                    stack[top-1] += stack[top]
                elif fx[i] == '-':
                    stack[top-1] -= stack[top]
                stack[top] = False
                top -= 1
            else:
                return 'error'
        else:
            top += 1
            stack[top] = int(fx[i])


T = int(input())
for case in range(1, T+1):
    fx = input().split()

    print(f'#{case}', forth(fx))
