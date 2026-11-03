class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        maxProfit = 0
        for price in prices:
            if price < buy:
                buy = price
                sell = price
            if price > sell:
                sell = price
                maxProfit = max(maxProfit, sell - buy)
        return maxProfit
            
        