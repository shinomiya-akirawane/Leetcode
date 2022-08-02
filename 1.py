class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    if i not in ans:
                        ans.append(i)
                    if j not in ans:
                        ans.append(j)
        return ans
s = Solution()
print(s.binarySearch([4,3,0],0,0))
print(s.twoSum([0,4,3,0],0))