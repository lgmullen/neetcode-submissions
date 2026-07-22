class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_num = nums[0]
        total = 0
        for num in nums:
            if num == current_num:
                total += 1
            else:
                total -= 1
            if total <= 0 and num != current_num:
                current_num = num
                total = 0
                print()
        return current_num

