# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        rev_dict = {}

        for i, j in enumerate(nums):

            compl = target - j
            if rev_dict.get(compl) or rev_dict.get(compl) == 0:
                return [rev_dict[compl], i]
            else:
                rev_dict[j] = i
