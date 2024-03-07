# 베이비진 게임
def f():
    vic = [0, 0]
    for x in range(10):
        if a[x]:
            if x+2 < 10 and a[x+1] and a[x+2]:
                vic[0] = 1
            elif a[x] >= 3:
                vic[0] = 1
        if b[x]:
            if x+2 < 10 and b[x+1] and b[x+2]:
                vic[1] = 1
            elif b[x] >= 3:
                vic[1] = 1
    if vic[0] and vic[1]:
        return 3
    elif vic[0]:
        return 1
    elif vic[1]:
        return 2
    return 0


T = int(input())
for case in range(1, T+1):
    num_list = list(map(int, input().split()))

    a = [0] * 10
    b = [0] * 10
    for i in range(12):
        if i % 2 == 0:
            a[num_list[i]] += 1
        else:
            b[num_list[i]] += 1
        if i >= 4:
            ans = f()
            if ans:
                if ans == 3:
                    ans = 0
                break

    print(f'#{case}', ans)
