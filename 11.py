class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        maxA = 0
        while l < r:
            if height[l]<height[r]:
                area = min(height[l],height[r])*(r-l)
                l += 1
            else:
                area = min(height[l],height[r])*(r-l)
                r -= 1
            maxA = max(maxA,area)
        return maxA
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))