class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        if len(s) <=1:
            return dict[s]
        ans += dict[s[0]]
        for i in range(1,len(s)):
            num = dict[s[i]]
            pre_num = dict[s[i-1]]
            if pre_num < num:
                ans -= pre_num
                ans += num-pre_num
            else:
                ans += num
        return ans
s = Solution()
print(s.romanToInt('MCMXCIV'))