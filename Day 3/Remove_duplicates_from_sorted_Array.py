# Problem URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 1 if nums[0] == nums[1] else 2
    
        main = 0
        
        swap = False
        
        for i in range(1, n):
            if nums[i] != nums[i-1] and not swap:
                main += 1
                nums[main] = nums[i]
                
                
            elif nums[i] != nums[i-1] and swap:
                nums[main] = nums[i]
                swap = False
                
            
            elif nums[i] == nums[i-1] and not swap:
                swap = True
                main += 1
                
        if swap:
            return main
        return main+1
                