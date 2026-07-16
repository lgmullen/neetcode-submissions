
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        self.res = 0

        def rec(i, largest, size):
            if i >= len(nums):
                return size
            res = rec(i+1, largest, size)
            if nums[i] > largest:
                res = max(res,rec(i+1, nums[i], size+1) )
            return res
        return rec(0,-100000,0)
            