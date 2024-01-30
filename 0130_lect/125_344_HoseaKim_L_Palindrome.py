def is_palindrome(word_str):
    if not(word_str.isalpha()):
        new_word = ''
        for i in word_str:
            if i.isalnum():
                new_word += i
        new_word = new_word.lower()
        return new_word == new_word[::-1]
    else:
        return word_str == word_str[::-1]


def rev_str(word_list):
    return word_list[::-1]


# word_str = input()
# print(is_palindrome(word_str))
word_list1 = ["h","e","l","l","o"]
word_list2 = ["H","a","n","n","a","h"]
print(rev_str(word_list1))
print(rev_str(word_list2))