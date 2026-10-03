class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {'}': '{', ')': '(', ']': '['}
        stack = []
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
        
        

        