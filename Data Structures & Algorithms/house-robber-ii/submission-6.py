class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        arr1 = nums[0:len(nums)-1]
        arr2 = nums[1:len(nums)]
        if len(arr1) == 1:
            return max(arr1[0], arr2[0])

        cache = [0] * len(arr1)
        cache[0] = arr1[0]
        cache[1] = max(cache[0], arr1[1])
        for i in range(2,len(arr1)):
            cache[i] = max(cache[i-2]+arr1[i], cache[i-1])
        arr_1_val = cache[-1]


        cache = [0] * len(arr2)
        cache[0] = arr2[0]
        cache[1] = max(cache[0], arr2[1])
        for i in range(2,len(arr2)):
            cache[i] = max(cache[i-2]+arr2[i], cache[i-1])
        arr_2_val = cache[-1]

        return max(arr_1_val, arr_2_val)