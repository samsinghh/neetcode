"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
we want to have a mapping from each old node to each new node
then, we do a dfs through the graph, and every time we get to
a node we haven't already made a copy of, we recursively create it 
'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping = {}

        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            clone = Node(node.val)
            mapping[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)


        