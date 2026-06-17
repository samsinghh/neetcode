# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binarySearch(self, root, target):
        arr = []
        while root:
            arr.append(root)
            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                return arr
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = self.binarySearch(root, p.val)
        q_ancestors = self.binarySearch(root, q.val)

        oldest = 0
        for node1, node2 in zip(p_ancestors, q_ancestors):
            if node1.val == node2.val:
                oldest = node1
        
        return oldest
        
    
    # [5, 3, 4]
    # [5, 3]
