class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for n,c in counts.items():
            buckets[c].append(n)


        res = []
        i = 0
        for b in reversed(buckets):
            for n in b:
                if i < k:
                    res.append(n)
                    i += 1
                else:
                    return res
        
        return res



        