class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        res_len = len(s)
        res = ""
        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for c in t:
            t_count[c] += 1
                
        letters_needed = len(t_count)

        for r in range(len(s)):
            s_count[s[r]] += 1

            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                letters_needed -= 1


            while letters_needed == 0:
                if r - l + 1 <= res_len:
                    print(s[l])
                    print(s[r])
                    res = s[l:r+1]
                    res_len = r - l + 1
                    print(res)

                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    letters_needed += 1
                l += 1
        
        return res
            




        
        