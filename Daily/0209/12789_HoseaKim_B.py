def dokidoki(n, num_list):

    goal = [0] * n
    stack = [0] * n
    cnt = 1
    top = -1
    for i in range(n):
        while stack[top] == cnt:
            goal[cnt-1] = cnt
            cnt += 1
            stack[top] = 0
            top -= 1
        if num_list[i] == cnt:
            goal[cnt-1] = cnt
            cnt += 1
        else:
            top += 1
            stack[top] = num_list[i]
    while stack[0]:
        if stack[top] == cnt:
            goal[cnt-1] = cnt
            cnt += 1
            stack[top] = 0
            top -= 1
        else:
            return 'Sad'
    return 'Nice'


n = int(input())
num_list = list(map(int, input().split()))

print(dokidoki(n, num_list))