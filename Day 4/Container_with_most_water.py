# Problem URL: https://leetcode.com/problems/container-with-most-water/submissions/
# Two pointer approach - TC: O(n), SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        
        maxarea = 0
        j = len(height) - 1

        while i != j:
            
            maxarea = max((j-i)*min(height[i], height[j]), maxarea)
            
            if height[i] >= height[j]:
                j -= 1
                
            else:
                i += 1
        
        return maxarea
        
        
        
        
# Brute Force TC: O(n^2), SC: O(1)
#         while i < n - 1:
#             j = i + 1
#             while j < n:
                
#                 area = (j-i) * min(height[i], height[j])
#                 if area > maxarea:
#                     maxarea = area
                    
#                 j += 1
                
#             i += 1
            
#         return maxarea