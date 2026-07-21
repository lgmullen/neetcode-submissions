class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(index, sub):
            # you can take it or naw
            if index == len(nums):
                res.append(sub)
            else:
                back(index+1, sub)
                back(index+1, sub + [nums[index]])
        back(0, [])
        return res