def calculator(fx_len, fx):

    stack = []
    ans = []
    for tk in fx:
        if tk == '+':
            if stack:
                stack.pop()
                x = ans.pop()
                ans[-1] += x
            stack.append(tk)
        else:
            ans.append(int(tk))
    return ans[0] + ans[1]


T = 10
for case in range(1, T+1):
    fx_len = int(input())
    fx = input()

    print(f'#{case}', calculator(fx_len, fx))
