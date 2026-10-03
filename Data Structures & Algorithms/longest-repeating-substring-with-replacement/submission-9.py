class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_val = max(counts.values())

            if (r - l + 1) - max_val <= k:
                res = max(res,r - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1
            
            
        return res
