# Problem URL: https://leetcode.com/problems/rotate-image/submissions

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        if n == 1:
            return matrix
        
        count = 0
        
        si, sj = 0,0
        ei, ej = n-1,n-1
        i, j = 0, n-1
        
        
        while si < ei:
            tmp = matrix[n-1-i][j]
            matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
            matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
            matrix[i][n-1-j] = matrix[j][i]
            matrix[j][i] = tmp
            
            i += 1
            if i == ei:
                si += 1
                j -= 1
                i = si
                ei -= 1
            
        return matrix
        