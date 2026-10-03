class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            num = str(len(s))
            res = res + num + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        j = 0
        res = []
        while i < len(s):
            print(res)
            print(f"i = {i}")
            print(f"j = {j}")
            word_len = ""
            while s[j] != "#":
                word_len += s[j]
                j += 1
            word_len = int(word_len)
            i = j
            j += 1
            word = ""
            while j-i <= word_len:
                word += s[j]
                j += 1
            res.append(word)
            i = j

        return res



