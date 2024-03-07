def color_rect(n, rect_list):

    

    return


T = int(input())
for case in range(1, T+1):
    n = int(input())
    rect_list = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case}', color_rect(n, rect_list))
