class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            res = dp(i+1, j) + dp(i, j+1)

            memo[(i,j)] = res
            return res
        return dp(0,0)
        
            

            

            
            
            