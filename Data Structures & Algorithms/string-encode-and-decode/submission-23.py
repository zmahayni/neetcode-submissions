class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        
        return res


    def decode(self, s: str) -> List[str]:

        #.  4#neet4#code4#love#3you

        res = []
        print(s)
        i = 0
        while i < len(s):
            j = i
            count = 0
            while j < len(s):
                if s[j] == "#":
                    count += int(s[i:j])
                    res.append(s[j+1:j+count+1])
                    j += count + 1
                    break
                else:
                    j+=1
            i = j
        
        return res
            
            




