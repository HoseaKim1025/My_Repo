def pizza(n, m, cheese):

    q = list(range(n))
    front = -1
    rear = 0
    index = n-1
    while rear != front:
        cheese[q[rear]] //= 2
        if cheese[q[rear]] == 0 and index < m-1:
            index += 1
            q[rear] = index
        front = rear
        rear = (rear + 1) % n
        while cheese[q[rear]] == 0:
            rear = (rear + 1) % n
        while cheese[q[front]] == 0:
            front = (front - 1) % n

    return q[front] + 1


T = int(input())
for case in range(1, T+1):
    # n : 화덕의 크기, m : 피자 개수
    n, m = map(int, input().split())
    # 각 피자의 치즈량
    cheese = list(map(int, input().split()))

    print(f'#{case}', pizza(n, m, cheese))
