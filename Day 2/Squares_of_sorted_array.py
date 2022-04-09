# URL: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if nums[-1] < 0:
            return [i*i for i in nums[::-1]]
        
        if nums[0] >= 0:
            return [i*i for i in nums]
        
        # def post(arr):
        #     low = 0
        #     high = len(arr)
        #     while low != high:
        #         if len(arr) < 2 or arr[0] >= 0 or arr[-1] < 0:
        #             break
        #         mid = (low + high) // 2
        #         if arr[mid] >= 0 and arr[mid-1] < 0:
        #             return mid
        #         elif arr[mid] > 0:
        #             high = mid
        #         elif arr[mid] < 0:
        #             low = mid + 1
        #     return -1
            
        tp = [i for i, j in enumerate(nums) if (j >= 0 and nums[i-1] < 0)][0]   # post(nums)
        neg = [i*i for i in nums[:tp][::-1]] # [25, 49 , 99980001, 100000000]
        pos = [i*i for i in nums[tp:]] # [0, 0, 100000000] 
        a = 0 # 0, 1, 2
        b = 0 # 0, 1, 2, 3
        f = []
        
        for i in range(len(nums)):
            if a == len(pos) and b == len(neg):
                break
            elif a == len(pos):
                f.append(neg[b])
                b += 1
                
            elif b == len(neg):
                f.append(pos[a])
                a += 1
                
            elif (pos[a]) <= (neg[b]):
                f.append(pos[a])
                a += 1
                
            elif (pos[a]) >= (neg[b]):
                f.append(neg[b])
                b += 1
                
        return f
                
                
        