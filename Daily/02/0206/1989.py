def palindrome(new_word):

    for i in range(len(new_word)//2):
        new_word[i], new_word[len(new_word)-1-i] = new_word[len(new_word)-1-i], new_word[i]

    return new_word


T = int(input())
for case in range(1, T+1):
    word = list(input())
    new_word = word[:]
    new_word = palindrome(new_word)
    if word == new_word:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
