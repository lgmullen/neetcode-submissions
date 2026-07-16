
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        self.res = 0

        def rec(i, largest, sub):
            print(i, largest,sub)
            if i >= len(nums):
                self.res = max(self.res,len(sub))
                return
            rec(i+1, largest, sub)
            if nums[i] > largest:
                rec(i+1, nums[i], sub+ [nums[i]])
            return
        rec(0,-100000,[])
        return self.res
            