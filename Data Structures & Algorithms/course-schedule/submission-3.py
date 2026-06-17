class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i : [] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            
            if len(prereqs[course]) == 0:
                return True
            
            visited.add(course)

            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True