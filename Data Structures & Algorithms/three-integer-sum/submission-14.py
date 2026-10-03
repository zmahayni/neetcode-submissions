class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

#[-1, -1, 0, 1, 2]

        nums.sort()
        res = []
        for i in range(len(nums)):

            target = 0 - nums[i]
            l = i+1
            r = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
            
        return res



            
        
        