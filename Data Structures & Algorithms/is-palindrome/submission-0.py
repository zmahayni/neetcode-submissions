class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ""

        for c in s:
            if c.isalnum():
                new_s += (str(c))
        new_s = new_s.lower()
        print(new_s)

        i = 0
        j = len(new_s) - 1

        for i in range(len(new_s)):
            if new_s[i] != new_s[j]:
                return False
            
            j-=1
            
        return True