class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {"(", "[", "{"}
        for c in s:
            if c in opening:
                stack.append(c)
            if stack == []:
                return False
            if c == ")" and stack.pop() != "(":
                    return False
            if c == "]" and stack.pop() != "[":
                    return False
            if c == "}" and stack.pop() != "{":
                    return False  
        # if stack != []:
        #     return False
        return not stack