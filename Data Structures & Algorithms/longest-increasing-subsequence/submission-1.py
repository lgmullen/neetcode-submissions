
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        self.res = 0

        def rec(i, largest, size):
            if i >= len(nums):
                self.res = max(self.res,size)
                return
            rec(i+1, largest, size)
            if nums[i] > largest:
                rec(i+1, nums[i], size+1)
            return
        rec(0,-100000,0)
        return self.res
            