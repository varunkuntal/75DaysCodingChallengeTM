# Problem URL: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # Optmized - TC: O(n), SC: O(1)
        n = len(time)
        ll = [0] * 60
        count = 0
                
        for i in range(n):
            mod = time[i] % 60
            res = 60 - mod
            
            count += ll[res] if mod != 0 else ll[0]
            
            ll[mod] += 1            
            
        return count
            
            
## Brute Force O(n^2), SC: O(1)
#         n = len(time)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if (time[i] + time[j]) % 60 == 0:
#                     count += 1
                    
                    
#         return count