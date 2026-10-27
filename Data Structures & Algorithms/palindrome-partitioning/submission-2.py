class Solution:
    def isPal(self,s,l,r):
            substring = s[l:r+1]
            if substring[::-1] == substring:
                return True
            return False
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        # partition
        
        def dfs(i, j):
            if i == len(s):
                res.append(part.copy())
                return
            if j == len(s):
                return
            
            # if its a palindrome
            if self.isPal(s, i, j):
                part.append(s[i:j + 1])
                # we move the start to the next partitiion i see
                dfs(j + 1, j + 1)
                part.pop()
            dfs(i,j+1)


        dfs(0,0)
        return res
