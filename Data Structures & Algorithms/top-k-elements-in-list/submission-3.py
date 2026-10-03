class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        counts = defaultdict(int)
        freqs = [[]for i in range(l+1)]
        res = []

        for n in nums:
            counts[n] += 1
        for c, n in counts.items():
            freqs[n].append(c)
        
        for i in range(len(freqs)-1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) >= k:
                    return res


        

