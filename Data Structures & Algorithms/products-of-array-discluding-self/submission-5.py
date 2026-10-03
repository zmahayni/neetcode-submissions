class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                prefix[i] = prefix[i-1] * nums[i-1]

        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue
            else:
                postfix[i] = postfix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res