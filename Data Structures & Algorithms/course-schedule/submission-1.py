class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for i in range(numCourses):
            premap[i] = []
        for course, pre in prerequisites:
            premap[course].append(pre)
        
        visited = set()
        

        def findCycle(course):
            if course in visited:
                return True
            visited.add(course)
            for child in premap[course]:
                if findCycle(child):
                    return True
            visited.remove(course)
            return False

        for c in range(numCourses):
            if findCycle(c):
                return False
        return True