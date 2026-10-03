class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in sums:
                solution = [sums[nums[i]], i]
                return solution
            else:
                sums[diff] = i

        return []
        