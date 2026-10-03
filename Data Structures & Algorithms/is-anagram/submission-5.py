class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for c in s:
            s_count[c] += 1
        for c in t:
            t_count[c] += 1
        
        if t_count == s_count:
            return True
        
        return False
