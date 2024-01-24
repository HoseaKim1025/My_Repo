word_in = input()
words = list(word_in.upper())
word_len = len(words)
word_set = list(set(words))
word_set_len = len(word_set)
most = [0]*word_set_len

for i in range(word_set_len):
    count = 0
    for j in range(word_len): # j = 
        if word_set[i] == words[j]:
            count += 1
    most[i] = count
count = 0

for i in most:
    if max(most) == i:
        count += 1
if count > 1:
    print('?')
else:
    print(word_set[most.index(max(most))])