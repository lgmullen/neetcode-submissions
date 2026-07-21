class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def dfs(index, sub, total):
            if total == target:
                res.append(sub)
                return
            if total > target:
                return
            if index >= len(nums):
                return 
            # do we add that ish or naw
            dfs(index, sub + [nums[index]], total + nums[index])
            dfs(index+1, sub, total)

        dfs(0,[], 0)
        return res
