class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        l = 0
        for r in range(len(prices)):
            if l == r:
                continue
            
            while prices[l] > prices[r] and l < r:
                l += 1
            
            profit = prices[r] - prices[l]
            res = max(profit, res)
        

        return res
            
            


        