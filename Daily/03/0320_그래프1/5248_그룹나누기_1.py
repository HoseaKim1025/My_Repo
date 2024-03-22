# 3월 20일 <그래프> 5248 그룹 나누기 풀이1 반복문
T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    group = [[] for _ in range(n+1)]

    for i in range(m):
        group[arr[i*2]].append(arr[i*2+1])
        group[arr[i*2+1]].append(arr[i*2])

    for i in range(1, n+1):
        j = 0
        while j < len(group[i]):
            if group[i][j] != i:
                group[i].extend(group[group[i][j]])
                group[group[i][j]] = []
            j += 1

    cnt = 0
    person = set(range(1, n+1))
    for i in range(1, n+1):
        if group[i]:
            person -= set(group[i])
            cnt += 1
    cnt += len(person)

    print(f'#{case}', cnt)
