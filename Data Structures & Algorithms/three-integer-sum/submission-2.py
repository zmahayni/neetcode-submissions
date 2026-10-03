class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            diff = 0 - nums[i]
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum > diff:
                    r-=1
                if curr_sum < diff:
                    l+=1
                if curr_sum == diff:
                    curr_arr = [nums[i], nums[l], nums[r]]
                    res.append(curr_arr)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1


        return res
        # res = []
        # nums.sort()

        # for i, a in enumerate(nums):
        #     if a > 0:
        #         break

        #     if i > 0 and a == nums[i - 1]:
        #         continue

        #     l, r = i + 1, len(nums) - 1
        #     diff = 0 - a
        #     while l < r:
        #         Sum = nums[l] + nums[r]
        #         if Sum > diff:
        #             r -= 1
        #         elif Sum < diff:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
                        
        # return res
           


                