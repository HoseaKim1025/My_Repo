def paper(n):
    # 1 : 20*10, 2: 20*20, 3: 10*20 *2
    top = 0
    stack = [[0, 0] for _ in range(n//10 + 1)]
    stack[0] = [1, 1]
    ans = 0
    while stack[1][0] < 4:
        ans += 1
        while top < n//10:
            if stack[top][0] == 1:
                top += 1
                stack[top][0] += 1
                stack[top][1] = 1
            if stack[top][0] == 2:
                top += 2



    return ans


T = int(input())
for case in range(1, T+1):
    n = int(input())

    rect1 = []

    print(f'#{case}', paper(n))
