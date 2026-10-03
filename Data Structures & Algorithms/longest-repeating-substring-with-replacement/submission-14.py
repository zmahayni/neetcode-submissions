class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        counts = defaultdict(int)

        l = 0
        max_count = 0

        for r in range(len(s)):
            curr_len = r - l + 1
            counts[s[r]] += 1

            max_count = max(max_count, counts[s[r]])
            while curr_len - max_count > k:
                counts[s[l]] -= 1
                l += 1
                curr_len -= 1
            
            res = max(res, curr_len)
            
        return res
