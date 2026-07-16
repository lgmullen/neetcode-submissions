class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums)-1:
                return True
            memo[i] = False
            for j in range(i+1,i + nums[i]+1):
                if dfs(j):
                    memo[i] = True
            return memo[i]
        return dfs(0)

