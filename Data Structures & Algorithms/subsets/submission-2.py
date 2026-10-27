class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def rec(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            rec(i + 1, sub)
            sub.pop()
            rec(i +1, sub)

        rec(0,[])
        return res