class Solution:
    def reverse(self, x: int) -> int:
        stringX = str(x)
        if '-' in stringX:
            reversedX = stringX[0] + (stringX[::-1])[:len(stringX)-1]
        else:
            reversedX = stringX[::-1]
        ansNum = int(reversedX)
        if ansNum>2**31-1 or ansNum <-2**31:
            return 0
        return ansNum

s = Solution()
s.reverse('-123')