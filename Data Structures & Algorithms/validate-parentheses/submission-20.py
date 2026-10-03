class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        parantheses_map = {']': '[', ')': '(', '}': '{'}

        for c in s:
            if c not in parantheses_map:
                stack.append(c)
            if c in parantheses_map:
                if not stack:
                    return False
                if stack[-1] != parantheses_map[c]:
                    return False
                else:
                    stack.pop()

        if stack:
            return False
        
        return True
        