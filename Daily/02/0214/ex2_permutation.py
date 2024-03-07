# 순열 만들기
'''
3
2 1 2
5 8 5
7 2 2
'''

''' ver1
def f(i, k):
    global min_v
    if i == k:
        # print(*p)
        s = 0   # 선택한 원소의 합
        for j in range(k):  # j행에 대해
            s += arr[j][p[j]]   # j행에서 p[j] 열을 고른 경우의 합 구하기
        if min_v > s :
            min_v = s
    else:
        for j in range(i, k):           # p[i] 자리에 올 원소 p[j]
            arr[i], arr[j] = arr[j], arr[i]     # p[i] <-> p[j]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]     # 교환 전으로 복구


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
p = list(range(n))
min_v = 100
f(0, n)
print(min_v)
'''

def f(i, k, s):
    global cnt
    global min_v
    cnt += 1
    if i == k:
        # print(*p)
        s = 0   # 선택한 원소의 합
        for j in range(k):  # j행에 대해
            s += arr[j][p[j]]   # j행에서 p[j] 열을 고른 경우의 합 구하기
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):           # p[i] 자리에 올 원소 p[j]
            p[i], p[j] = p[j], p[i]     # p[i] <-> p[j]
            f(i+1, k, s+arr[i][p[i]])
            p[i], p[j] = p[j], p[i]     # 교환 전으로 복구


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
p = list(range(n))
min_v = 100
cnt = 0
f(0, n, 0)
print(min_v, cnt)
