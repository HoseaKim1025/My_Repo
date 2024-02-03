class Solution:
    def groupAnagrams(self, strs):
        strs_len = len(strs)
        set_list = [0] * strs_len
        str_dict = {}
        for i in range(strs_len):
            set_list[i] = sorted(strs[i])
            str_dict[f'{set_list[i]}'] = []
        new_list = list(zip(set_list, strs))
        for j in new_list:
            str_dict[f'{j[0]}'].append(j[1])
        
        return list(str_dict.values())
    

# strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
strs = ["ddddddddddg","dgggggggggg"]
a = Solution()
print(a.groupAnagrams(strs))
# [["bat"],["nat","tan"],["ate","eat","tea"]]
# [[""]]
# [["a"]]