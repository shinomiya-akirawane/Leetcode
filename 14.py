class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for str in strs:
            if len(prefix) < len(str):
                prefix = str
        for word in strs:
            prefix = prefix[0:min(len(prefix),len(word))]
            for i in range(0,min(len(prefix),len(word))):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix
s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))