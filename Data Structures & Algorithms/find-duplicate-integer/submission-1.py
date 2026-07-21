class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = nums[abs(nums[i])-1]
            if index < 0:
                print("hey")
                print(nums)
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
        return -1