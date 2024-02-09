class Solution:
    def productExceptSelf(self, nums):
        nums_len = len(nums)

        ans = [1] * nums_len

        for i in range(1, nums_len):
            ans[i] *= ans[i-1] * nums[i-1]

        temp = nums[nums_len-1]
        
        for i in range(nums_len-2, -1, -1):
            ans[i] *= temp
            temp *= nums[i]
            
        return ans


nums = [1,2,3,4]
a = Solution()
print(a.productExceptSelf(nums))
