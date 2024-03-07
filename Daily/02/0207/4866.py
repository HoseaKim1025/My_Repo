def bracket(in_str):
    stack = [0] * len(in_str)
    bracket_in = {'(': 1, '{': 2, '[': 3}
    bracket_out = {')': 1, '}': 2, ']': 3}
    top = -1
    for i in in_str:
        if i in bracket_in:
            idx_in = bracket_in[i]
            top += 1
            stack[top] = idx_in
        elif i in bracket_out:
            idx_out = bracket_out[i]
            if stack[top] == 0 or stack[top] != idx_out:
                return 0
            else:
                stack[top] = 0
                top -= 1
    if stack[0]:
        return 0
    else:
        return 1


T = int(input())
for case in range(1, T+1):
    in_str = input()

    print(f'#{case}', bracket(in_str))
