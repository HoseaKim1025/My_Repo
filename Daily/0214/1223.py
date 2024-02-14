def postfix_changer(n, fx):

    priority = {'*': 2, '+': 1}
    postfix = ''
    top = -1
    stack = [0] * n
    for x in fx:
        if x in priority:
            while stack[top] and priority[x] <= priority[stack[top]]:
                postfix += stack[top]
                stack[top] = 0
                top -= 1
            top += 1
            stack[top] = x
        else:
            postfix += x
    while stack[top]:
        postfix += stack[top]
        top -= 1

    return postfix


def calculator(n, postfix):

    top = -1
    stack = [-1] * n
    for tk in postfix:
        if tk == '*':
            stack[top-1] *= stack[top]
            stack[top] = -1
            top -= 1
        elif tk == '+':
            stack[top - 1] += stack[top]
            stack[top] = -1
            top -= 1
        else:
            top += 1
            stack[top] = int(tk)

    return stack[0]


T = 10
for case in range(1, T+1):
    n = int(input())
    fx = input()
    postfix = postfix_changer(n, fx)

    print(f'#{case}', calculator(n, postfix))
