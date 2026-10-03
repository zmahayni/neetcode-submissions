class Solution:
    def isValid(self, s: str) -> bool:
        
        par_pairs = {']':'[', '}':'{',')':'('}
        stack = []
        for c in s:
            if c not in par_pairs:
                stack.append(c)
            else:
                if not stack or stack.pop() != par_pairs[c]:
                    return False

        if stack:
            return False
        return True
        
                