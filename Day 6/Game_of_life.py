# Problem URL: https://leetcode.com/problems/game-of-life

class Solution:
    def validateNeighbours(self, board, start, r, c):

        score = 0
        # Right, Down, Left and Right
        adj = [[start[0], start[1]+1] if start[1]+1 < c else False, [start[0]+1, start[1]] if start[0]+1 < r else False, [start[0], start[1]-1] if start[1]-1 > -1 else False, [start[0]-1, start[1]] if start[0]-1 > -1 else False]

        adj_d = [[start[0]-1, start[1]-1] if start[1]-1 > -1 and start[0]-1 > -1 else False, [start[0]-1, start[1]+1] if start[0]-1 > -1 and start[1]+1 < c else False, [start[0]+1, start[1]+1] if start[1]+1 < c and start[0]+1 < r else False, [start[0]+1, start[1]-1] if start[0]+1 < r and start[1]-1 > -1 else False]


        for i in adj:
            if i:
                score += board[i[0]][i[1]]

        for j in adj_d:
            if j:
                score += board[j[0]][j[1]]

        
        return score
    
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        
        r, c = len(board), len(board[0])
        
        scoreboard = [[0]*c for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                scoreboard[i][j] = self.validateNeighbours(board, [i,j], r, c)
                
        for i in range(r):
            for j in range(c):
                if scoreboard[i][j] < 2 or scoreboard[i][j] > 3:
                    board[i][j] = 0
                if scoreboard[i][j] == 3:
                    board[i][j] = 1
                    
        return board
                    
                    
                    
                    
                    
                    