class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        cnt = 0
        max_len = 1
        ans = 1
        for letter in s:
            max_len = 1
            cnt += 1
            substring = '' + letter
            for letter2 in s[cnt:]:
                if letter2 in substring :
                    break
                else:
                    max_len += 1
                    substring += letter2
            if max_len > ans:
                ans = max_len
            max_len = 1
        return ans
s = Solution()
print(s.lengthOfLongestSubstring('abcegsaacc'))