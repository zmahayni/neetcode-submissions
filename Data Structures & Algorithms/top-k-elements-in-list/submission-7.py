class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums)+1)] 

        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        for num in counts:
            freq = counts[num]
            buckets[freq].append(num)
        
        print(buckets)
        res = []
        i = 0
        for bucket in reversed(buckets):
            for num in bucket:
                if i >= k:
                    break
                res.append(num)
                i += 1
        
        return res


        


