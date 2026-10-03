class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        
        for s in strs:
            s_count = [0] * 26
            for c in s:
                s_count[ord(c) - ord('a')] += 1
            anagrams[tuple(s_count)].append(s)
        

        res = list(anagrams.values())
        return res
            
