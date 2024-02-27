# 베이비진 게임
def f(i):
    p = list(range(i+1))
    a.add(num_list[i])
    b.add(num_list[i+1])
    f(i+2)


T = int(input())
for case in range(1, T+1):
    num_list = list(map(int, input().split()))

    a = set()
    b = set()
    f(0)

    print(f'#{case}', )
