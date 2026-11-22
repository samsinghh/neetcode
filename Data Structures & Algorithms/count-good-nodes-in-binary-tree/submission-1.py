# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def search(node, currMax):
            nonlocal res
            if node.val >= currMax:
                currMax = node.val
                res += 1
            
            if node.left:
                search(node.left, currMax)
            if node.right:
                search(node.right, currMax)
        
        search(root, float('-inf'))
        return res