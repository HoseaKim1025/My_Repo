n = int(input())
card_list = input().split()
m = int(input())
num_list = input().split()

exists = set(card_list) & set(num_list)

exists_dict = dict(zip(exists, [1]*len(exists)))

# card_dict = dict(zip(card_list, [1]*n))
num_dict = dict(zip(num_list, [0]*m))

num_dict.update(exists_dict)

# ans = card_dict.setdefault(10, 0)

print(*num_dict.values())