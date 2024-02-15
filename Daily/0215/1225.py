def password(data_list):

    rear = 0
    cnt = 1
    while data_list[rear-1] > 0:
        data_list[rear] -= cnt
        rear = (rear + 1) % 8
        if cnt == 5:
            cnt = 0
        cnt += 1
    data_list[rear-1] = 0
    ans = data_list[rear:] + data_list[:rear]

    return ans


for _ in range(10):
    case = input()
    data_list = list(map(int, input().split()))

    print(f'#{case}', *password(data_list))
