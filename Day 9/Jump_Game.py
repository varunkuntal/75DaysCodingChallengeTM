# Problem URL: https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        i = 0
        k = 0
        maxx = 0
        
        if n == 1:
            return True

        while True:
            
            while i <= k:
                maxx = max(maxx, i+nums[i])
                i += 1
                
            i = k + 1
            k = maxx
            
            if k >= n-1:
                return True
            
            if i > k:
                return False
                
                
        