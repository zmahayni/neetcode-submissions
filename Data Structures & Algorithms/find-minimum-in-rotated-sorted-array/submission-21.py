class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1


        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[r]:
            return nums[0]

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= nums[r]:
                if nums[m-1] < nums[m]:
                    r = m - 1
                else:
                    return nums[m]
            else:
                l = m + 1
        
        return -1
        




        


        