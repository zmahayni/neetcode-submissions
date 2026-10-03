class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = 1
        streak = 1
        i = 0

        while i < len(nums) - 1:
            if nums[i+1] == nums[i]:
                # duplicate, skip
                i += 1
                continue
            elif nums[i+1] == nums[i] + 1:
                streak += 1
            else:
                streak = 1

            res = max(res, streak)
            i += 1

        return res
