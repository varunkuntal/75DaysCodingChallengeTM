# Problem URL: https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix)-1, len(matrix[0])-1
        lr, lc = 0, -1
        hr, hc = m, n
        i, j = 0, 0
        increment = 'c' if n != 0 else 'r'
        direction = 'p'
        collector = []
        total = (m+1) * (n+1)
        
        while True:
            
            collector.append(matrix[i][j])
            
            if len(collector) == total:
                break
            
            if increment == 'c' and direction == 'p':
                j += 1
            elif increment == 'r' and direction == 'p':
                i += 1
                
            elif increment == 'c' and direction == 'n':
                j -= 1
            elif increment == 'r' and direction == 'n':
                i -= 1
                
                
            if j == hc and increment == 'c':
                increment = 'r'
                lc += 1
                
            elif i == hr and increment == 'r':
                lr += 1
                increment  = 'c'
                direction = 'n'
                
            elif j == lc and increment == 'c':
                hc -= 1
                increment = 'r'
                
            elif i == lr and increment == 'r':
                increment = 'c'
                hr -= 1
                direction = 'p'
            
                
        return collector
            