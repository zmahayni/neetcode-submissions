class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set:
                count = 0
                while n in nums_set:
                    n+=1
                    count +=1
                res = max(count, res)

        return res

            
