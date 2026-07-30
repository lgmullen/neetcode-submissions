class Solution:
    #climb 0 stiar == 1
    # climb 1 stair == 1
    # clibm 2  = 2
    #climb 3 = 
    dp = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.dp:
            return self.dp[n]
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.dp[n] = res
        return res
