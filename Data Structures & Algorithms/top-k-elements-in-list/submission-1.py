class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        solution = []
        for n in nums:
            counts[n] += 1
        sorted_by_count = sorted(counts.keys(), key=counts.get, reverse=True)
        i = 0
        while (i < k):
            solution.append(sorted_by_count[i])
            i += 1
        return solution
