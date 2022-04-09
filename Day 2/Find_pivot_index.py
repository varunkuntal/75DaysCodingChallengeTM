# URL: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cum_sum = [nums[0]]
        rev_cum_sum = [nums[-1]]

        for i in range(1, len(nums)): # i = 1,2,3,4,5  ||  nums = 1,7,3,6,5,6
            cum_sum.append(nums[i] + cum_sum[i-1]) # [1,8,11,17,22,28]
            rev_cum_sum.append(nums[len(nums)-1-i] + rev_cum_sum[i-1]) # [6,11,17,20,27,28]
            
        for i in range(len(cum_sum)):
            if cum_sum[i] == rev_cum_sum[len(cum_sum) - 1 - i]:
                return i

        return -1
            
        
            
        