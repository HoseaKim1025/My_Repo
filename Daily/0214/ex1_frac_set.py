# 부분집합 만들기

'''
# ver 1
def f(i, k, t): # k개의 원소를 가진 배열 a, 부분집합 합이 t인 경우를 찾음
    if i == k:  # 모든 원소에 대해 결정하면
        ss = 0  # 부분 집합 원소의 합
        for j in range(k):
            if bit[j]:  # a[j]가 포함된 경우
                # print(a[j], end=' ')
                ss += a[j]
        # print('=', ss)

        if ss == t:
            for j in range(k):
                if bit[j]:  # a[j]가 포함된 경우
                    print(a[j], end=' ')
            print()         # 부분집합 출력
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)


n = 10
a = list(range(1, 11))
bit = [0] * n   # bit[i]는 a[i]가 부분집합에 포함되는지 표시
f(0, n, 10)
'''

# ver2
def f(i, k, s, t): # i-1 원소까지 고려한 합 s -> s가 t를 넘어가면 더이상 고려한 필요 X
    global cnt
    cnt += 1
    if s == t:
        for j in range(k):
            if bit[j]:  # a[j]가 포함된 경우
                print(a[j], end=' ')
        print()         # 부분집합 출력
    elif i == k:    # 모든 원소를 고려했으나 s != t
        return
    elif s > t:     # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, t)
        bit[i] = 1
        f(i+1, k, s+a[i], t)
        bit[i] = 0
        f(i+1, k, s, t)


n = 10
a = list(range(1, 11))
bit = [0] * n
cnt = 0
f(0, n, 0, 10)
print('cnt :', cnt)
