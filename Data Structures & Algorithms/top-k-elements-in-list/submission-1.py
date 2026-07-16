class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] = count.get(num,0) + 1
        for key, value in count.items():
            freq[value].append(key)
        for i in range(len(freq)-1,-1,-1):
            frequency = freq[i]
            if frequency:
                for item in frequency:
                    res.append(item)
                    if len(res) == k:
                        return res

        return []

        