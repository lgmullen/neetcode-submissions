class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = dict()
        for char in s:
            seen[char] = seen.get(char,0) + 1
        for char in t:
            if char in seen:
                seen[char] -= 1
                if seen[char] == 0:
                    del seen[char]
            else:
                return False
        return len(seen) == 0