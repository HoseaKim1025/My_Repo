class Solution:
    def trap(self, height):
        h_len = len(height)
        total = 0
        for i in range(h_len):
            temp_sum = 0
            if height[i] > 0 and height[i] :
                for j in range(i+1, h_len):
                    if height[i] > height[j]:
                        temp_sum += height[i] - height[j]
                    else:



        return

height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = Solution()
print(a.trap(height))