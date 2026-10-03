class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy_date = 0
        sell_date = 1
        while sell_date < len(prices):
            if prices[buy_date] < prices[sell_date]:
                profit = prices[sell_date] - prices[buy_date]
                max_profit = max(max_profit, profit)
            else:
                buy_date = sell_date
            sell_date += 1
            
        return max_profit
            
            
            
            


            




        