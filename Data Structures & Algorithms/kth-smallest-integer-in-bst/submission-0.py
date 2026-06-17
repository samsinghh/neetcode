# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        checker = 0
        self.res = 0
        def dfs(root, k):
            nonlocal checker 
            if root:
                dfs(root.left, k)
                checker += 1
                if checker == k:
                    self.res = root.val
                
                dfs(root.right, k)
        
        dfs(root, k)
        return self.res
