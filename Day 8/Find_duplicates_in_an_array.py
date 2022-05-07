class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 1
        ll = []
        n = len(nums)
        while i <= n:
            if nums[i-1] == i:
                i += 1
            elif nums[nums[i-1]-1] == nums[i-1]:
                ll.append(nums[i-1])
                i += 1
            else:
                nums[i-1], nums[nums[i-1]-1] = nums[nums[i-1]-1], nums[i-1]
                
        return ll
                
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