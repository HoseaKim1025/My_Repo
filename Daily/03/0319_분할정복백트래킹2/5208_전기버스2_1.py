# 3월 19일 <병합정복, 백트래킹> 5208 전기버스2 풀이1 반복문
T = int(input())
for case in range(1, T+1):
    in_list = list(map(int, input().split()))
    n, m = in_list[0], in_list[1:]
    i = 0
    cnt = 0
    while i + m[i] < n-1:
        max_nxt = 0
        idx = i
        for j in range(i+1, i+m[i]+1):
            nxt = j + m[j]
            if max_nxt < nxt:
                max_nxt = nxt
                idx = j
        i = idx
        cnt += 1

    print(f'#{case}', cnt)
