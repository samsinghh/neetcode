class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        q = deque() 
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        completed = 0 
        while q:
            course = q.popleft()
            for after in adj[course]:
                indegree[after] -= 1
                if indegree[after] == 0:
                    q.append(after)
            completed += 1
        
        return completed == numCourses



            