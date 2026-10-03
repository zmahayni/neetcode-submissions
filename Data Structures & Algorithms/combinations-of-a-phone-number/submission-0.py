class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToLetter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        
        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return None
            if len(curr) == len(digits):
                res.append(curr)
                return curr
            for l in digitToLetter[digits[i]]:
                next_string = curr + l
                dfs(i+1, next_string)

        dfs(0, '')
        return (res)
            

        