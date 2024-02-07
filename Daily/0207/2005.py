def pascal(n):
    tri = [1]
    print(*tri)
    cnt = 1
    while cnt < n:
        cnt += 1
        new_tri = [1] * cnt
        for i in range(cnt-1):
            if i + 1 < cnt - 1:     # < 3
                new_tri[i+1] = tri[i] + tri[i+1]
        tri = new_tri
        print(*tri)


T = int(input())
for case in range(1, T+1):
    n = int(input())

    print(f'#{case}')
    pascal(n)
