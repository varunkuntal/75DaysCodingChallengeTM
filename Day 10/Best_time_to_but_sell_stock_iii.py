# Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        totalprofit = []
        high = 0
        appended = True
        n = len(prices)
        
        for i in range(n):
            if prices[i] - minprice < profit:
                totalprofit.append(high - minprice)
                minprice = prices[i]
                profit = 0
                appended = True
                
            elif prices[i] - minprice > profit:
                profit = prices[i] - minprice
                high = prices[i]
                appended = False
                
        if not appended:
            totalprofit.append(high - minprice)
                
        first, second = -1, -1
        
        for i in totalprofit:
            if i >= first:
                second = first
                first = i
                
        first = max(0, first)
        second = max(0, second)
        
        return first + second