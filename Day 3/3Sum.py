# Problem URL: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        final = {}
        nums.sort()

        for i in range(n-2):

            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j != k:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    final[(nums[i], nums[j], nums[k])] = 1
                    if res - nums[i] > 0:
                        k -= 1
                    else:
                        j += 1
                    continue

                elif res > 0:
                    k -= 1

                else:
                    j += 1
                    
            if nums[i] == nums[i-1]:
                i += 1
                
                                  
        return final.keys()
                                  
                
#         # Brute Force O(n^3)
#         final = {}
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         boundary = min(nums[i], nums[j], nums[k]), max(nums[i], nums[j], nums[k])
#                         final[(boundary[0], -boundary[1]-boundary[0], boundary[1])] = 1
                        
#         return final.keys()
        