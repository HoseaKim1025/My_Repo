x = int(input())

def find_fraction(x):
    if x == 1:
        return 1
    count = 0
    fraction = [1, 1]
    for _ in range(x-1):
        i = 0
        j = 1
        if fraction[0] < fraction[1]:
            fraction[0] += 1
            fraction[1] -= 1
            i = 1
            j = -1
        elif fraction[0] > fraction[1]:
            fraction[0] -= 1
            fraction[1] += 1
            i = -1
            j = +1
        else:
            fraction[0] += i
            fraction[1] += j
        # print(f'{fraction[0]}/{fraction[1]}')
    return f'{fraction[0]}/{fraction[1]}'

print(find_fraction(x))