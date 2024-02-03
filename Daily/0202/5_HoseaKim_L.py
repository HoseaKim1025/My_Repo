class Solution:
    def longestPalindrome(self, s):
        s_len = len(s)
        word_len = 0
        max_len = 0
        ans = s[0]
        if s_len == 1:
            return s
        for i in range(s_len):
            if i+1 < s_len and s[i] == s[i+1]:
                word_len = 2
                R = i+1
                L = i
                if max_len < word_len:
                    max_len = word_len
                    ans = s[L:R+1]
                while L > 0 and R < s_len-1:
                    L -= 1
                    R += 1
                    if s[L] == s[R]:
                        word_len += 2
                        if max_len < word_len:
                            max_len = word_len
                            ans = s[L:R+1]
                    else:
                        if max_len < word_len:
                            max_len = word_len
                            ans = s[L:R+1]
                        break

            if i+2 < s_len and s[i] == s[i+2]:
                word_len = 3
                R = i+2
                L = i
                if max_len < word_len:
                    max_len = word_len
                    ans = s[L:R+1]
                while L > 0 and R < s_len-1:
                    L -= 1
                    R += 1
                    if s[L] == s[R]:
                        word_len += 2
                        if max_len < word_len:
                            max_len = word_len
                            ans = s[L:R+1]
                    else:
                        if max_len < word_len:
                            max_len = word_len
                            ans = s[L:R+1]
                        break

        return ans

s = "aaaa"
a = Solution()
print(a.longestPalindrome(s))