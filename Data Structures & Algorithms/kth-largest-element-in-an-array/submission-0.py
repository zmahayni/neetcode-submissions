class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-s for s in nums]
        res = []
        heapq.heapify(maxHeap) 
        while k > 0:
            res.append(-heapq.heappop(maxHeap))
            k-=1
        return res[-1]

            

            


        


        