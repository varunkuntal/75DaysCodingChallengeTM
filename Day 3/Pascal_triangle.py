class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = [[1]]
        i = 1

        while i < numRows:
            k = 0
            pt.append([1]) 
            while k+1 < len(pt[i-1]):
                pt[i].append(pt[i-1][k] + pt[i-1][k+1]) 
                k += 1
            pt[i].append(1)
            i += 1

        return pt
                
                's