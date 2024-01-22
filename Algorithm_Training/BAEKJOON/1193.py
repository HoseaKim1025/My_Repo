'''
# x까지 그냥 다 구해버리는 코드
x = int(input())

def fraction(x):
    if x == 1:
        return '1/1'
    else:
        frac = [1, 1]
        right = 0
        down = 0
        for i in range(x-1):
            if frac[0] == 1:
                if right != 1:
                    right = 1
                    down = 0
                    frac[1] += 1
                    continue
                else:
                    direction = [1, -1]
            elif frac[1] == 1:
                if down != 1:
                    right = 0
                    down = 1
                    frac[0] += 1
                    continue
                else:
                    direction = [-1, 1]
            frac[0] += direction[0]
            frac[1] += direction[1]
        return f'{frac[0]}/{frac[1]}'

print(fraction(x))
'''

# x가 몇 번째 바퀴인지 확인해서 그 바퀴부터 필요한 만큼만 구하는 코드
x = int(input())

# x가 몇 번째 바퀴인지(n), 그 바퀴 전까지 몇 개의 분수가 있었는지(sn) 판별
n = 0
while True:
    n += 1
    sn = (n*(n+1))/2
    if x <= sn:
        sn = int(((n-1)*n)/2)
        break
# x가 n번째 바퀴에 있고 그 전까지 sn개의 분수가 있었음
    
# n이 짝수면 1,n에서부터 x-1-n번 +1 -1
if n % 2 == 0:
    frac = [1, n]
    for _ in range(x-1-sn):
        frac[0] += 1
        frac[1] -= 1

# n이 홀수면 n,1에서부터 x-1-n번 -1 +1
else:
    frac = [n, 1]
    for _ in range(x-1-sn):
        frac[0] -= 1
        frac[1] += 1

print(f'{frac[0]}/{frac[1]}')