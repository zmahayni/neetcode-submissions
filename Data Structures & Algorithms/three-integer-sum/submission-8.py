class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        #. -4, -1, -1, 0, 1, 2
        
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i-1] == n:
                continue
            
            target = 0 - n
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([n, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    l+=1
        return res
                