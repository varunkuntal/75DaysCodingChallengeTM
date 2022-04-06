class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count =  m * n
        negative_count = 0

        p,q = 0, 0

        while True:
            if grid[p][q] < 0:
                negative_count += 1

            if q % n == n - 1:
                p += 1
                q = 0
                if p == m:
                    break
                continue


            q += 1

        return negative_count