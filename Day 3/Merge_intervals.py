# Problem URL: https://leetcode.com/problems/merge-intervals/solution/

class Solution:
    # 3 Pointer approach, TC: O(nlogn) SC: O(1) (inplace)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        
        if n == 1:
            return intervals
        
        intervals.sort()
        main = 0
        i = 1
        inplace = 0
        
        while i < n:                
            if intervals[main][1] <= intervals[i][1] and intervals[main][1] >= intervals[i][0]:
                intervals[main][1] = intervals[i][1]
                
            elif intervals[main][1] < intervals[i][0]:
                intervals[inplace] = intervals[main]
                main = i
                inplace += 1
            
            i += 1
            
        if intervals[main] not in intervals[:inplace+1]:
            intervals[inplace] = intervals[main]
            
        inplace += 1
            
        return intervals[:inplace]