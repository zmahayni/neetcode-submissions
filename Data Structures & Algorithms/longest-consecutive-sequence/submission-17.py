class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set()
        print(sorted(nums))
        res = 0

        for n in nums:
            nums_set.add(n)
        
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                n = nums[i] + 1
                curr = 0
                while n - 1 in nums_set:
                    curr += 1
                    n += 1
                    res = max(res, curr)

        
        return res
                
