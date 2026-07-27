class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()
        # without duplicate
        for r in range(len(s)):
            char = s[r]
            while char in seen:  
                seen.remove(s[l])
                l += 1
            seen.add(char)
            print(seen, l)
            res = max(r-l+1, res)
                

        return res



