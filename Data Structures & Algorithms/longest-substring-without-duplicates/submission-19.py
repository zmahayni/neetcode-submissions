class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        l = 0
        r = 0
        curr = set()
        while r < len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            
            curr.add(s[r])
            r += 1
            res = max(len(curr), res)
        
        return res

            