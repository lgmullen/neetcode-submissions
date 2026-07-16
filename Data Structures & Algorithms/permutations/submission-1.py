class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        def dfs(sub, pick):
            if len(sub) == length:
                print("here")
                res.append(sub.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    sub.append(nums[i])
                    pick[i] = True
                    dfs(sub, pick)
                    sub.pop()
                    pick[i] = False
                
        dfs([], [False] * len(nums))

        return res
        
                