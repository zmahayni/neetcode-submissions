class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = 0
        i = 1

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[r]:
            return nums[0]

        while l <= r:
            m = (l + r) // 2
            print(f'l = {l}, r = {r}, m = {m}')

            if nums[m] <= nums[r]:
                if nums[m-1] == nums[m] - 1:
                    print(f'{i}, at 1')
                    r = m - 1
                else:
                    print(f'{i}, at 2')
                    return nums[m]
            else:
                print(f'{i}, at 3')
                l = m + 1
                
            i += 1
        
        return -1
        


        


        

        


        