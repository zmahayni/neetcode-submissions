class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            m = (l + r) // 2
            print(f'l = {l}, m = {m}, r = {r}')
            res = min(res, nums[l])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1
        
        return res



