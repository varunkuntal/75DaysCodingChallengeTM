# Problem URL: https://leetcode.com/problems/3sum-closest/submissions/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        mini_total = 0
        mini = float('inf')
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                i+= 1
                
            j = i+1
            k = n-1

            while j != k:
                total = nums[i] + nums[j] + nums[k]
                res = total - target
                if abs(res) < abs(mini):
                    mini = res
                    mini_total = total
                if res > 0:
                    k -= 1
                elif res < 0:
                    j += 1
                else:
                    return mini_total
        return mini_total
        
        
        
##        Brute Force O(n^3) - TLE 101/132
#         n = len(nums)
#         delta = float('inf')
#         closest = float('inf')
#         for i in range(n-2):
#             for j in range(i+1,n-1):
#                 for k in range(j+1, n):
#                     total = nums[i] + nums[j] + nums[k]
#                     res = abs(total - target)
#                     if res < delta:
#                         delta = res
#                         closest = total
                        
#         return closest

