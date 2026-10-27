class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(i, sub):
            if i == len(nums):
                res.append(sub)
                return
            rec(i + 1, sub + [nums[i]])
            rec(i +1, sub)
            return 
        rec(0,[])
        return res