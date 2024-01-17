word = list(input())
rev = []
for i in range(len(word)):
    rev.append(word[len(word)-1-i])
print(int(word == rev))