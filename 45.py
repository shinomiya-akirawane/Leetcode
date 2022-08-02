def jump(nums: list[int]) -> int:
        ans = []
        if len(nums) == 1:
            return 0
        for num in nums:
            ans.append(0)
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= len(nums)-1:
                ans[i] += 1
            else:
                ans[i] = 10000000
                for j in range(i,nums[i]+i+1):
                    ans[i] = min(ans[i],ans[j] +1)
        return ans[0]

print(jump([1,1,1,1]))