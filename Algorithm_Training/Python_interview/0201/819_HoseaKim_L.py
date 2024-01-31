import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        word = re.sub(r"[^a-zA-Z]", " ", paragraph)
        word = word.lower().split()
        
        word_set_list = list(set(word) - set(banned))
        most = 0
        most_word = ''
        for i in word_set_list:
            cnt = word.count(i)
            if most < cnt:
                most = cnt
                most_word = i
            
        return most_word
    
'''
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

a = Solution()
print(a.mostCommonWord(paragraph, banned))
'''