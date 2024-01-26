
m, n = map(int, input().split())

anti_prime = set()
for i in range(m, n+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            anti_prime.add(i)
            break
prime = set(range(m, n+1)) - anti_prime
print(*sorted(prime), sep='\n')

'''
m, n = map(int, input().split())

flag = 0
for i in range(m, n+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)
'''