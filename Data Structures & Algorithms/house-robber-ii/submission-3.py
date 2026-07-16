class Solution:
    def rob(self, nums: List[int]) -> int:
        arr1 = nums[1:]
        arr2 = nums[:-1]
        def dp(i, arr, memo):
            if i in memo:
                return memo[i]
            if i >= len(arr):
                return 0
            memo[i] = max(dp(i+1, arr, memo), arr[i] + dp(i+2, arr, memo))
            return memo[i]

        first = dp(0, arr1, {})
        second = dp(0, arr2, {})
        if len(nums) == 1:
            return nums[0]
        return max(first, second)

            
