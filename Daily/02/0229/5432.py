# 쇠막대기 자르기
T = int(input())
for case in range(1, T+1):
    loc = input()

    # stack = [0] * len(loc)
    # top = -1
    # ss = 0
    # for i in loc:
    #     # '(' 만나면 append (쇠막대기 한 개)
    #     if i == '(':
    #         top += 1
    #         stack[top] += 1
    #     # ')' 만나면 pop
    #     else:
    #         # 직전 쇠막대기가 한 번도 잘리지 않았으면
    #         # (=해당 () 쌍이 레이저라는 뜻)
    #         if stack[top] == 1:
    #             stack[top] = 0
    #             for j in range(top):
    #                 stack[j] += 1
    #             top -= 1
    #         # 직전 쇠막대기가 한 번이라도 잘렸으면
    #         # (=해당 ()쌍이 쇠막대기라는 뜻)
    #         else:
    #             ss += stack[top]
    #             stack[top] = 0
    #             top -= 1

    cnt = 0
    for i in range(len(loc)):
        if loc[i] == '(':


    print(f'#{case}', ss)
