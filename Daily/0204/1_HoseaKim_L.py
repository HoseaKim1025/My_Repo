class Solution:
    def twoSum(self, nums, target):
        '''
        nums_len = len(nums)
        for i in range(1 << nums_len):
            sum_nums = 0
            cnt = 0
            ans = []
            for j in range(nums_len):
                if i & 1 << j:
                    sum_nums += nums[j]
                    cnt += 1
                    ans.append(j)

            if cnt == 2 and sum_nums == target:
                return ans
        '''
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [0,4,3,0]
target = 0
a = Solution()
print(a.twoSum(nums, target))