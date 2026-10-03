class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        l = 0
        r = 1

        # for r in range(len(prices)):

        while l < len(prices) and l < r and r < len(prices):
            curr = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            res = max(curr, res)
            r += 1
        
        return res

            
        