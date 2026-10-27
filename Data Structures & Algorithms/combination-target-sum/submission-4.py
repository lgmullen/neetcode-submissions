class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def dfs(index, sub, total):
            # yes
            if total > target:
                return 
            if index >= len(nums):
                return
            if total == target:
                res.append(sub)
                return
            # ok we can take it or just go to the next one

            dfs(index, sub + [nums[index]], total + nums[index])
            dfs(index+1, sub, total)
            # dont take it 
            return

           
        dfs(0,[], 0)
        return res
