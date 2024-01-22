t = int(input())
c_list = list(int(input()) for _ in range(t))

# 동전별 센트
quater = 25
dime = 10
nickel = 5
penny = 1

# 거스를 동전 개수 판별
result = []
for c in c_list:
    q, c = divmod(c, quater)
    d, c = divmod(c, dime)
    n, c = divmod(c, nickel)
    p, c = divmod(c, penny)
    temp = q, d, n, p
    result.append(temp)

# test case 별로 출력 ('q d n p' 형태로 출력 -> 리스트 언패킹)
for i in range(t):
    print(*result[i])