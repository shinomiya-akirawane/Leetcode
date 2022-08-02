class Solution:
    def climbStairs(self, n: int) -> int:
        med = [0,1,2]
        for i in range(3,n+1):
            med.append(med[i-1] + med[i-2])
        return med[n]

s = Solution()
s.climbStairs(3)