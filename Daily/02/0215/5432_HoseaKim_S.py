def cut(in_str):

    top = -1
    stack = [0] * 100000
    ans = 0
    pre = 0
    for i in in_str:
        if i == '(':
            if pre == '(':
                stack[top] += 1
                top += 1
            elif pre == ')' or pre == 0:
                top += 1
        elif i == ')':
            if pre == '(':
                for j in range(top):
                    stack[j] += 1
                top -= 1
            elif pre == ')':
                ans += stack[top]
                stack[top] = 0
                top -= 1
        pre = i

    return ans


T = int(input())
for case in range(1, T+1):
    in_str = input()

    print(f'#{case}', cut(in_str))
