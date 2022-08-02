class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = nums[l]+nums[r]
                if sum < 0-nums[i]:
                    l += 1
                elif sum > 0-nums[i]:
                    r -= 1
                else:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
        return ans
s = Solution()
print(s.threeSum([0]))