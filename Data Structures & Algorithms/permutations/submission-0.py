class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(added):
            if len(added) == len(nums):
                res.append(added[:])
                return
            for n in nums:
                if n not in added:
                    added.append(n)
                    dfs(added)
                    added.pop()
                    
        dfs([])
        return res

                

        