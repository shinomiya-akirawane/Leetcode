def maxSubArray(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    ans = nums
    for i in range(1,len(nums)):
        ans[i] = max(ans[i-1] + nums[i],ans[i])
    return max(ans)
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))