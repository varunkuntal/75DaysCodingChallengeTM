# Problem URL: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Brute Force O(n^3)
        final = {}
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        boundary = min(nums[i], nums[j], nums[k]), max(nums[i], nums[j], nums[k])
                        final[(boundary[0], -boundary[1]-boundary[0], boundary[1])] = 1
                        
        return final.keys()
        