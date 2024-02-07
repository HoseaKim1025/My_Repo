def remove(in_str):
    stack = [''] * 1000
    top = -1
    for i in in_str:
        if stack[top] == i:
            stack[top] = ''
            top -= 1
        else:
            top += 1
            stack[top] = i
        # print(''.join(stack))

    return len(''.join(stack))


T = int(input())
for case in range(1, T+1):
    in_str = input()

    print(f'#{case}', remove(in_str))
