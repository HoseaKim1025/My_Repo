class Solution:
    def maxProfit(self, prices):

        prices_len = len(prices)
        min_num = 10000
        max_num = 0
        profit = max_num - min_num

        for i in range(prices_len):

            if min_num > prices[i]:
                min_num = prices[i]
                max_num = 0

            if max_num < prices[i]:
                max_num = prices[i]

            if profit < max_num - min_num:
                profit = max_num - min_num

        return profit


prices = [2,4,1]
a = Solution()
print(a.maxProfit(prices))