class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target:
                 return
            if cur == target:
                res.append(path.copy())
                return
            if idx >= len(candidates):
                return
            
            # you can take it or not 
            path.append(nums[idx])
            dfs(idx+ 1, path, cur + nums[idx])
            path.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
            dfs(idx + 1, path, cur)



        dfs(0, [], 0)
        print(res)
        return res