class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        d = {}
        n = len(nums)

        while i < n:
            if nums[i] == i+1:
                i += 1
            elif nums[nums[i]-1] == nums[i]:
                d[nums[i]] = 1
                i += 1
            else:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp

        return d.keys()
                
## Naiive solution TC: O(n), SC: O(n)
#         d = {}
#         dd = {}
#         for i in nums:
#             if d.get(i):
#                 d[i] += 1
#                 dd[i] = 1
#             else:
#                 d[i] = 1
                
#         return dd.keys()