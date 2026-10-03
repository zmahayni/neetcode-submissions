class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            s_lower = s.lower()
            for c in s_lower:
                count[ord(c) - ord('a')] += 1
            res_map[tuple(count)].append(s)
        
        return list(res_map.values())
            
        

                

