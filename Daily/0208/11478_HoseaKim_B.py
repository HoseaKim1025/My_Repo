s = input()

s_len = len(s)
s_set = set()
for i in range(1, s_len):
    for j in range(0, s_len-i+1):
        s_set.add(s[j:j+i])

print(len(s_set)+1)