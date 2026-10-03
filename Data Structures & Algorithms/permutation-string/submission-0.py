class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        l = 0
        for r in range (len(s2)):
            print(l)
            print(r)
            sub_count = [0] * 26
            substring = s2[l:r+1]
            if len(substring) < len(s1):
                r +=1
                continue
            print(substring)
            for c in substring:
                sub_count[ord(c) - ord('a')] += 1
            if sub_count == s1_count:
                return True
            else:
                l += 1

        return False

        