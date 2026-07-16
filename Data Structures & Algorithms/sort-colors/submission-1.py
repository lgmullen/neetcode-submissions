class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            print(nums,i,j)
        n = len(nums)
        red = 0
        white = 0
        blue = 0
        for i in range(n):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else: 
                blue += 1
        l = 0
        while l < red:
            nums[l] = 0
            l+=1
        while l  < red + white:
            nums[l] = 1
            l+=1
        while l < n:
            nums[l] = 2
            l += 1
        

        

        print(nums)