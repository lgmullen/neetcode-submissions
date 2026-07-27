class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.Counter()
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1
            maxf = max(maxf,freq[s[r]])
            while (r-l+1) - maxf > k:
                freq[s[l]] -= 1
                l+= 1
            res = max(r-l+1, res)
        return res



            