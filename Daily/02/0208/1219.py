def find_path(n, line_list):
    top = 0
    stack = [-1] * n
    stack[0] = 0
    while stack[0] == 0:
        flag = 0
        for i in range(n):
            if line_list[i][0] == stack[top]:
                top += 1
                stack[top] = line_list[i][1]
                line_list[i] = [-2, -2]
                flag = 1
                break
        if stack[top] == 99:
            return 1
        if flag == 0:
            stack[top] = -1
            top -= 1

    return 0


for case in range(1, 11):
    t, n = map(int, input().split())    # t : 테스트케이스, n : 길의 개수
    in_line = list(map(int, input().split()))
    line_list = [0] * n
    for i in range(n):
        line_list[i] = [in_line[i*2], in_line[i*2+1]]

    print(f'#{case}', find_path(n, line_list))
