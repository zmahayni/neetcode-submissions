class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums)+1)] 

        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        for num in counts:
            freq = counts[num]
            buckets[freq].append(num)
        
        res = []

        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        


        


