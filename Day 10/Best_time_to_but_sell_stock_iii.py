# Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minprice = prices[0]
        profit = 0
        tp = 0
        n = len(prices)
        streaks = []
        high = 0
        
        for i in range(1, n):
            res = prices[i] - prices[i-1]
            if res > 0:
                high = prices[i]
                
            elif res < 0:
                if prices[i] < minprice:
                    streaks.append(high - minprice)
                    minprice = prices[i]
                    high = 0

        streaks.append(high - minprice)
        
        first, second = -1, -1
        for i in streaks:
            if i > first:
                second = first
                first = i
                
        first = max(0, first)
        second = max(0, second)
        
        return first + second
        