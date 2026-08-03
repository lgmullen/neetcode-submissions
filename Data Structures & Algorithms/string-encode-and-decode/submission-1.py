class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length)
            res += "#"
            res += word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        j = i
        while i < len(s):
            while s[j] != '#':
                j+= 1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        return res
            

        
            
