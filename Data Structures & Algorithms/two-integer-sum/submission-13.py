class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        needed = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in needed:
                first = min(needed[diff], i)
                second = max(needed[diff], i)
                return [first, second]
            else:
                needed[n] = i
        return [-1]
