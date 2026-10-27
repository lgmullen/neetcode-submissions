class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        sub = []

        def dfs(index, sub, total):
            # yes
            if total > target:
                return 
            if index >= len(nums):
                return
            if total == target:
                res.append(sub.copy())
                return
            # ok we can take it or just go to the next one

            dfs(index+1, sub, total)
            sub.append(nums[index])
            dfs(index, sub, total + nums[index])
            sub.pop()
            # dont take it 
            return

           
        dfs(0,[], 0)
        return res
