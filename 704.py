class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l<r:
            mid = ((l+r)//2)
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        return -1
#   return True if len(set(nums)) != len(nums) else False
s = Solution()
print(s.search([1,2,3,4,5],2))