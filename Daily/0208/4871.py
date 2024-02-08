def path(v, e, node_line_list, s, g):

    top = 0
    stack = [0] * v
    stack[0] = s
    while stack[0] != 0:
        flag = 0
        for i in range(e):
            if node_line_list[i][0] == stack[top]:
                top += 1
                stack[top] = node_line_list[i][1]
                node_line_list[i][0] = node_line_list[i][1] = 0
                flag = 1
                break
        if stack[top] == g:
            return 1
        if flag == 0:
            stack[top] = 0
            top -= 1

    return 0


T = int(input())
for case in range(1, T+1):
    v, e = map(int, input().split())    # v : 노드 개수, e = 간선 개수
    node_line_list = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())    # s : 시작 노드, g = 도착 노드

    print(f'#{case}', path(v, e, node_line_list, s, g))
