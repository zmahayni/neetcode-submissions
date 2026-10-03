class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        

        have = 0
        need = len(t_map)
        res = [-1,-1]
        resLen = float('inf')

        s_map = defaultdict(int)

        l = 0
        for r in range(len(s)):
            c = s[r]
            s_map[c] += 1

            if c in t_map and s_map[c] == t_map[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r-l+1
                    res=[l,r]
                s_map[s[l]] -=1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''
