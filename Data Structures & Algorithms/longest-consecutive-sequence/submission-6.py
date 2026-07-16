class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            j = num
            while j <= len(nums) and j in numSet:
                longest = max(longest, j-num+1)
                j+=1
        return longest
                
