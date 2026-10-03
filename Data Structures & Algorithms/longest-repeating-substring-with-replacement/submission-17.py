class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_count = 0
        curr_map = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            curr_map[s[r]] += 1
            max_count = max(max_count, curr_map[s[r]])

            while (r - l + 1) - max_count > k:
                curr_map[s[l]] -= 1
                l += 1
                curr_len = r - l + 1

            res = max(res, r - l + 1)

        return res
            




        