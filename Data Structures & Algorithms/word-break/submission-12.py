class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def rec(i):
            if i >= len(s):
                return True
            if i in dp:
                return dp[i]

            res = False
            for j in range(i, len(s)+1):
                if s[i:j] in wordDict and rec(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return rec(0)


            

       
            
