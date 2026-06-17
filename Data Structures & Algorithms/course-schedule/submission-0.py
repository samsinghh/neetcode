class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i : [] for i in range(numCourses)}

        for first, second in prerequisites:
            prereqs[first].append(second)
        
        visited = set()

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
            prereqs[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                


