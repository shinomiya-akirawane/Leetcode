class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        brackets = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        for letter in s:
            if letter == '[' or letter == '(' or letter == '{':
                top+=1
                stack.append(letter)
            else:
                if stack[top] == brackets[letter]:
                    stack.pop(top)
                    top -= 1
                
        return stack == []

c = Solution()
print(c.isValid('(])'))