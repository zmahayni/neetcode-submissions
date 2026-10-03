class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inArray = set()

        for n in nums:
            if n in inArray:
                return True
            else:
                inArray.add(n)
        
        return False