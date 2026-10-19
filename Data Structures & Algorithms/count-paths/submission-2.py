class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            if i == m-1 and j == n-1:
                res = 1
            elif i < m and j < n:
                res = dp(i+1, j) + dp(i, j+1)
            elif j < n:
                res = dp(i, j+1)
            elif i < m:
                res = dp(i+1, j)
            memo[(i,j)] = res
            return res
        return dp(0,0)
        
            

            

            
            
            