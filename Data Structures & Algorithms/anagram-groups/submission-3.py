class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arrays = []
        for i in range(len(strs)):
            s_arr = []
            s = strs[i]

            s_already_in_array = False
            if arrays is not None:
                for arr in arrays:
                    if s in arr:
                        s_already_in_array = True
            if s_already_in_array:
                continue

            s_arr.append(s)
            s_map = defaultdict(int)
            for k in s:
                s_map[k] += 1
            for j in range(len(strs)):
                if j<=i:
                    continue
                other_s = strs[j]
                other_s_map = defaultdict(int)
                for k in other_s:
                    other_s_map[k] += 1
                if s_map == other_s_map:
                    s_arr.append(other_s)
            arrays.append(s_arr)
                    
        return arrays


        
        