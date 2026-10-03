class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            count = str(len(s))
            res += count
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while i < len(s):
            num_s = ""
            while s[j] != '#':
                num_s += s[j]
                j += 1
            i = j+1
            num = int(num_s)
            j = i + num
            new_string = s[i:j]
            i = j
            res.append(new_string)
        return res
        


