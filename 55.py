def canJump(nums: list[int]) -> bool:
    maxIndex = 0
    for i in range(0,len(nums)):
        if i <= maxIndex:
            maxIndex = max(maxIndex,i+nums[i])
            if maxIndex >= len(nums):
                return True
    return False

print(canJump([0]))