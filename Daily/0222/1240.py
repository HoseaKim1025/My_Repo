# 단순 2진 암호코드
def find_start():
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if arr[i][j] == 1:
                return [i, j]


def find_password():
    rule = [
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1]
    ]
    scan = []
    password = []
    i = 0
    for i in range(end[1]-55, end[1], 7):
        for j in range(7):
            scan.append(arr[end[0]][i + j])
        for num in range(10):
            if scan == rule[num]:
                password.append(num)
                scan = []
                break
        else:
            return 0

    test = 0
    for i in range(0, 7, 2):
        test += password[i]
    test *= 3
    for i in range(1, 8, 2):
        test += password[i]

    ans = 0
    if not test % 10:
        for i in range(8):
            ans += password[i]

    return ans


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]

    end = find_start()

    print(f'#{case}', find_password())
