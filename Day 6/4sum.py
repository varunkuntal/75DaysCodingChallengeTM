# Problem URL: https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        d = {}
        
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                a, b = j+1, n-1
                while a != b:
                    ll = [nums[i], nums[j], nums[a], nums[b]]
                    ll.sort()
                    total = sum(ll)
                    if total == target:
                        d[tuple(ll)] = 1
                        if total - nums[i] - nums[j] > target:
                            b -= 1
                        else:
                            a += 1
                        continue
                        
                    if total > target:
                        b -= 1
                        
                    elif total < target:
                        a += 1
                        
        return d.keys()
                
        
        
        
## Brute Force TC: O(n^4)
#         n = len(nums)
#         c = {}
        
#         if n < 4:
#             return []
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     for l in range(k+1, n):
#                         ll = [nums[i], nums[j], nums[k], nums[l]]
#                         total = sum(ll)
#                         ll.sort()
                        
#                         if total == target:
#                             c[(ll[0], ll[1], ll[2], ll[3])] = 1
                            
#         return c.keys()