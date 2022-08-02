class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        start = 0
        if s == '':
            return 0
        if s[0] == '-':
            sign = '-'
            start += 1
        elif s[0] == '+':
            sign = '+'
            start += 1
        else:
            sign = '+'
        num = ''
        for letter in s[start:]:
            if ord(letter) > ord('9') or ord(letter) < ord('0'):
                break
            num += letter
        if num == '':
            return 0
        if sign == '+':
            num = int(num)
        elif sign == '-':
            num = int('-'+num)
        if num > 2**31-1:
            num = 2**31-1
        elif num < -2**31:
            num = -2**31
        return num
s = Solution()
print(s.myAtoi("+-42"))
