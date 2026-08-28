# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# root node can be any number, has no limit
# anything to left of root node MUST be smaller than it
# anything to the right of the root node MUST be larger than it
# 2
#1 4
#. 3
# base case, if node is None, return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(node, lower, upper):
            if not node:
                return True
            
            if not (lower < node.val < upper):
                return False
            
            return search(node.left, lower, node.val) and search(node.right, node.val, upper)
        
        return search(root, float('-inf'), float('inf'))
