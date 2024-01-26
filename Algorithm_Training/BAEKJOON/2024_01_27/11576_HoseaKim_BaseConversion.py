base_a, base_b = map(int, input().split())
a_len = int(input())
a_list = list(map(int, input().split()))
q = 0

for i in range(a_len):
    q += a_list[i] * base_a ** (a_len - 1 - i)
if base_b == 10:
    print(*str(q))
else:
    result = []
    while True:
        q, r = divmod(q, base_b)
        result.append(r)
        if q < base_b:
            result.append(q)
            break

    print(*result[::-1])