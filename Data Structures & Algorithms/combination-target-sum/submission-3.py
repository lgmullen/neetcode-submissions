class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def dfs(index, sub, total):
            if total == target:
                res.append(sub.copy())
                return
            if total > target or index >= len(nums):
                return
            sub.append(nums[index])
            dfs(index, sub, total + nums[index])
            sub.pop()
            dfs(index+1, sub, total)

        dfs(0,[], 0)
        return res
