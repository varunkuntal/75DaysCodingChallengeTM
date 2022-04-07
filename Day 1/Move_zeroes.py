# https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                continue
            for j in range(i, length):
                if nums[j] == 0:
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                break

        return nums
      

    