def permute(nums: list[int]) -> list[list[int]]:
    ans = []
    temp = ['' for x in range(0,len(nums))]
    used = {}
    for num in nums:
        used[num] = 0
    def dfs(temp,nums):
        if len(temp) == len(nums):
            ans.append(temp)
            return
        for i in range(0,len(nums)):
            if used[nums[i]] == 0:
                newTemp = temp+[nums[i]]
                used[nums[i]] = 1
                dfs(newTemp,nums)
                used[nums[i]] = 0
            else:
                continue
    dfs([],nums)
    return ans
print(permute([1,2,3]))
'''
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = []
        ans = []
        for num in nums:
            used.append(0)
        def dfs(curr,exceptLen,ans):
            if len(curr) == exceptLen:
                ans.append(curr)
                curr = []
            for i in range(0,len(nums)):
                if used[i] == 0:
                    curr.append(nums[i])
                    used[i] = 1
                    dfs(curr,exceptLen,ans)
                    used[i] = 0
        return ans
'''