class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        def dfs(i):
            print(i)
            if i >= len(nums)-1:
                return True
            for j in range(i+1,i + nums[i]+1):
                print(j)
                if dfs(j):
                    return True
            return False
        return dfs(0)

