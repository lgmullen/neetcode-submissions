class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        water = 0
        while l < r:
            # current water lolz
            area = min(heights[l], heights[r]) * (r-l)
            water = max(water, area)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return water