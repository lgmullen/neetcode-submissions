class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total1 = 0
        for i in range(0,n+1):
            total1 += i
        total = sum(nums)
        return total1 - total

        