class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}

        for bracket in s:
            #checks at the closing bracket and if the mru bracket is opposite to it
            if bracket in closeToOpen: # checks the close brackets
                if stack and closeToOpen[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(bracket)
        return True if not stack else False #