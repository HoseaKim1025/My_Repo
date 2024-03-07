class Solution:
    def twoSum(self, nums, target):
        
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [0,4,3,0]
target = 0
a = Solution()
print(a.twoSum(nums, target))