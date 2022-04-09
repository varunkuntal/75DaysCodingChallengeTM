# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minprice = float('inf')
        totalprofit = 0
        
        for i in range(len(prices)):
            if prices[i] - minprice < profit:
                totalprofit += profit
                profit = 0
                minprice = prices[i]

            elif prices[i] - minprice > profit:
                profit = prices[i] - minprice
                
        totalprofit += profit
        return totalprofit
                

            