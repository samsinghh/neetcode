class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        res = []
        curr, visited = set(), set()

        def dfs(course):
            if course in curr:
                return False
            
            if course in visited:
                return True
            
            curr.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            curr.remove(course)
            visited.add(course)
            res.append(course)
            return True
    

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
        