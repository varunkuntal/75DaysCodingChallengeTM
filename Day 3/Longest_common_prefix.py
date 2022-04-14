# Problem URL: https://leetcode.com/problems/longest-common-prefix/solution/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]
        
        ix = -1
        exit = False
        while not exit:
            ix += 1
            for i in range(n-1):
                try:
                    if strs[i][ix] != strs[i+1][ix]:
                        exit = True
                        break
                except:
                    exit = True
                    break
            

        if ix > 0:
            return strs[0][:ix]
        return ""