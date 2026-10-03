class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x == y:
                continue
            elif x > y:
                val = x - y
                heapq.heappush(maxHeap, -val)
            else:
                val = y - x
                heapq.heappush(maxHeap, -val)
        
        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        
        return 0

        

        
        