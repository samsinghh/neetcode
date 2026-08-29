# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if not abs(leftHeight - rightHeight) <=  1:
                self.balanced = False
            
            return 1 + max(leftHeight, rightHeight)
        
        dummy = dfs(root)

        return self.balanced