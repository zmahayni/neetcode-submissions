class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res_map = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))
            res_map[s_sorted].append(s)
        
        return list(res_map.values())

                

