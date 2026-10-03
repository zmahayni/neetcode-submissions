class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range (len(nums)):
            n = nums[i]
            x = target - n
            if x in vals:
                return [vals[x], i]
            else:
                vals[n] = i

