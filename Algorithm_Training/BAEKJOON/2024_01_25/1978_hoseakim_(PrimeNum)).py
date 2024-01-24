n = int(input())
in_list = set(map(int, input().split()))

no_prime_set = {1}
for i in range(2, max(in_list)):
    for j in range(i, max(in_list)):
        if i*j > max(in_list):
            break
        no_prime_set.add(i*j)
prime_set = in_list - no_prime_set
print(len(prime_set))