class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #create an adjacency matrix
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1
        
        for i in range(1, n + 1):
            print(incoming[i], outgoing[i])
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i
        return -1