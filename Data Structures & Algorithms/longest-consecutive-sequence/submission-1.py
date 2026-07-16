class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in range(len(nums)):
            curLength = 0
            cur = nums[i]
            while cur in numSet:
                cur += 1
                curLength+=1
                longest = max(longest, curLength)
        return longest

