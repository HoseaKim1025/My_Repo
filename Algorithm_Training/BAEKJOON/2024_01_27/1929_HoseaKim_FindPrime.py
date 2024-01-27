'''
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


for i in range(m, n+1):
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break

    else:
        print(i)