class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        res = 0
        while l <= r:

            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
            else:
                if target < nums[m] or target >= nums[l]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
        
    
        return -1