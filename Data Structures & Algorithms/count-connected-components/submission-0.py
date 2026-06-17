class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = {i: [] for i in range(n)}
        visited = set()
        for first, second in edges:
            adjacency[first].append(second)
            adjacency[second].append(first)
        

        def dfs(node):
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        res = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        
        return res
