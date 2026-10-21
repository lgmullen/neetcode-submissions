class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1 
        total = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            total_height = min(leftMax, rightMax)
            if leftMax < rightMax:
                l += 1
                total += (max(leftMax - height[l],0))
            else:
                r -= 1
                total += max((rightMax - height[r]),0)
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])

        return total
