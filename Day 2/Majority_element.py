# URL: https://leetcode.com/problems/majority-element/solution/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {x:nums.count(x) for x in set(nums)}
        for i in d.keys():
            if d[i] > len(nums) // 2:
                return i

            