class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        l = 0
        curr_set = set()
        for r in range(len(s)):
            while s[r] in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[r])

            curr = r - l + 1
            res = max(res, curr)
        
        return res


            
