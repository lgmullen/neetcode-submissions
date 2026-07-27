class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        mp = {}
        # without duplicate
        for r in range(len(s)):
            char = s[r]
            if char in mp:  
                l = max(mp[char]+1, l)
            mp[char] = r
            res = max(r-l+1, res)
        return res



