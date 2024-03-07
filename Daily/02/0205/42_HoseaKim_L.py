class Solution:
    def trap(self, height):
        h_len = len(height)
        L = 0
        R = h_len - 1
        L_max = 0
        R_max = 0
        total = 0
        while L < R:

            if L_max < height[L]:
                L_max = height[L]
            if R_max < height[R]:
                R_max = height[R]

            if L_max >= R_max:
                total += R_max - height[R]
                R -= 1
            else:
                total += L_max - height[L]
                L += 1

        return total


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
a = Solution()
print(a.trap(height))