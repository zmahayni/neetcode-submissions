class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0
        if len(num_set) == 1:
            return 1
        if nums is None:
            return 0
        for n in num_set:
            if n-1 not in num_set:
                count = 1
                while n+count in num_set:
                    count += 1
                    longest = max(count, longest)
        return longest
        