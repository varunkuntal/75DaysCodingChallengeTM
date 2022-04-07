# Problem URL
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        newmin = [10001, -1]
        newmax = [-1, -1]
        
        oldmin = [10001, -1]
        oldmax = [-1, -1]
                
        for i, j in enumerate(prices):
            
            if newmin[0] > j:
                newmin[0] = j
                newmin[1] = i
                newmax = [-1, -1]
                
            if newmax[0] < j:
                newmax[0] = j
                newmax[1] = i
                
                if newmax[0] > newmin[0] and newmax[1] > newmin[1]:
                    score = newmax[0] - newmin[0]
                    if score > (oldmax[0] - oldmin[0]):
                        oldmax = newmax.copy()
                        oldmin = newmin.copy()
                 
        if oldmax[0] > oldmin[0] and oldmax[1] > oldmin[1]:
            return oldmax[0] - oldmin[0]
        else:
            return 0
                
        