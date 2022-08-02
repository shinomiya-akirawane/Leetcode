class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_substring_length = len(s)
        for curr_substring_length in range(max_substring_length,-1,-1):          
            for start_index in range(0,len(s)-curr_substring_length+1):
                end_index = start_index+curr_substring_length-1
                substring = s[start_index:end_index+1]
                if substring == substring[::-1]:
                    return substring