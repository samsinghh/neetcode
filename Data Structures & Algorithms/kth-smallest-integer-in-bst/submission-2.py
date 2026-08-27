# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# do an in order traversal, track number of nodes visited, return when that number equals k

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0
        res = 0
        def search(node):
            nonlocal visited
            nonlocal res
            if not node:
                return
            
            search(node.left)
            visited += 1
            if visited == k:
                res = node.val
                return
            search(node.right)

        search(root)
        return res
                

        