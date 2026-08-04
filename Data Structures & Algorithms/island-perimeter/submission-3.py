class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #each island is 4 - whatever one it touches
        rows = len(grid)
        cols = len(grid[0])
        perimiter = 0
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        # there is 1 island
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimiter += 4
                    grid[i][j] == 0
                    for x,y in moves:
                        di = i + y
                        dj = j + x
                        if di < 0 or dj<0 or di>= rows or dj >= cols:
                            continue
                        if grid[di][dj] == 1:
                            print("here", di,dj)
                            perimiter -= 1
        return perimiter
                
                    
