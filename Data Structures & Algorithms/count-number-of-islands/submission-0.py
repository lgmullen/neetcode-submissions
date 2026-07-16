class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        self.islands = 0
        def dfs (i, j, grid):
            grid[i][j] = "X"
            # i is row, j is column
            moves = [(0,1),(1,0),(-1,0), (0,-1)]
            for di,dj in moves:
                # change in y ok 
                newI = i + di
                # change in X == column
                newJ = j + dj
                print(newI, newJ)
                if (0 <= newI < rows) and (0 <= newJ < cols) and grid[newI][newJ] == "1":
                    dfs(newI,newJ, grid.copy()) 
            return

                


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.islands +=1
                    dfs(i,j, grid)
        return self.islands

