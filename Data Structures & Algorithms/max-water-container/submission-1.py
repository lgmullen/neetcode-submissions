class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        water = 0
        while l < r:
            # current water lolz
            horizontal = r-l
            current = min(heights[l], heights[r]) * horizontal
            print(current)
            water = max(water, current)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return water