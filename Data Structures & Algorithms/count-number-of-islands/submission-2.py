class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        self.islands = 0
        moves = [(0,1),(1,0),(-1,0), (0,-1)]
        def dfs (i, j, grid):
            if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0"):
                return
            grid[i][j] = "0"
            for di,dj in moves:
                dfs(i + di, j + dj, grid.copy()) 
            return

                


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.islands +=1
                    dfs(i,j, grid)
        return self.islands

