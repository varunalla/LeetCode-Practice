class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyDay = 0
        sellDay = 1
        maxProfit = 0
        
        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
            else:
                buyDay = sellDay
            sellDay += 1
        
        return maxProfit
        
