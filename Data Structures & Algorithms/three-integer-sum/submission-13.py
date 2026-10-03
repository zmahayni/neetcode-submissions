class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        solutions = set()
        nums.sort()
        for i in range(len(nums)):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    solutions.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        print(solutions)
        for sol in solutions:
            res.append(list(sol))
        return res

        