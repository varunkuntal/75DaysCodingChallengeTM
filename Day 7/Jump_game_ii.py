# Problem URL: https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        jump = 0        
        n = len(nums)
        
        while j < n-1:
            max_jump = 0
            for a in range(i, j+1):
                max_jump = max(max_jump, a+nums[a])
                                
            i = j + 1
            j = max_jump
            jump += 1
            
        return jump