# Problem URL: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        maxx = -1
        
        total = sum(cardPoints[0:k])
        
        for i in range(k+1):
            if maxx < total:
                maxx = total
                
            total = total - cardPoints[k-1-i] + cardPoints[n-1-i]
        
        return maxx
        
#         # Brute Force O(n^2)
#         n = len(cardPoints)
#         maxx = -1
#         for i in range(k+1):
#             total = sum(cardPoints[0:k-i] + cardPoints[n-1:n-1-i:-1])
            
#             if total > maxx:
#                 maxx = total
                
#         return maxx
            
                