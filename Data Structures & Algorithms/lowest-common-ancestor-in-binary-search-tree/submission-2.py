# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def canReach(node: TreeNode, val):
            if not node:
                return False
            if node.val == val:
                return True
            if canReach(node.left, val) or canReach(node.right, val):
                return True
            return False
        res = None 
        qu = deque([root])
        while qu:
            for _ in range(len(qu)):
                node = qu.popleft()
                if canReach(node, p.val) and canReach(node, q.val):
                    res = node
                    if node.left:
                        qu.append(node.left)
                    if node.right:
                        qu.append(node.right)
        return res

            
            
