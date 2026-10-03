class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}
        res = []

        for i in range(len(nums)):
            curr = nums[i]
            if curr in m:
                return sorted([i, m[curr]])
            diff = target - nums[i]
            m[diff] = i
        

            


        