class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        # when opening found add 
        for char in s:
            if char in brackets: #check if it is a closing
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else: # it is opening
                stack.append(char)

        return True if not stack else False