class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res_set = set()
        
        def dfs(arr, curr_sum):
            if curr_sum == target:
                sorted_arr = sorted(arr[:])
                res_set.add(tuple(sorted_arr))
                return
            if curr_sum > target:
                return
            
            for n in nums:
                arr.append(n)
                curr_sum += n
                dfs(arr, curr_sum)
                arr.pop()
                curr_sum -= n

        dfs([], 0)
        res = []
        for t in res_set: 
            res.append(list(t))      

        return res 
            


            

        