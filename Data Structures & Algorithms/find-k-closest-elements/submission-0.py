class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the k closest elements to X
        l = 0
        r = len(arr) - 1
        # find the window

        while r - l >= k:
            if abs(arr[l]-x) <= abs(arr[r]-x):
                r -=1
            else:
                l+=1
        return arr[l:r+1]

