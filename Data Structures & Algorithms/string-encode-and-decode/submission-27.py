class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            num = str(len(s))
            res = res + num + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while i < len(s):
            word_len = ""
            while s[j] != "#":
                word_len += s[j]
                j += 1
            word_len = int(word_len)
            i = j+1
            j = i+word_len
            res.append(s[i:j])
            i = j

        return res



