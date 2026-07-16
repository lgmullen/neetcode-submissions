class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        # needs to be length 3 interesting

        def dfs(sub, remaining, i):
            print(sub)
            if len(sub) == len(nums):
                res.append(sub)
                return
            for i in range(0, len(remaining)):
                val = remaining[i]
                dfs(sub + [val], remaining[:i] + remaining[i+1:], i)
        dfs([], nums, 0)
        return res
        
                