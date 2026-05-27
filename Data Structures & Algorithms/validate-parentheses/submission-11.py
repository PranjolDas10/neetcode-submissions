class Solution:
    def isValid(self, s: str) -> bool:
        #if odd number it is false
        #divide the string in half
        #insert that half into a stack with closing form
        # if ([{ enter )]}
        # that should match with second half of string
        stack = []
        length = len(s)
        if length % 2 != 0 or length == 0:
            return False
        for x in range(0, length):
            if s[x] == '(':
                stack.append(')')
            elif s[x] == '[':
                stack.append(']')
            elif s[x] == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != s[x]:
                    return False
        return not stack