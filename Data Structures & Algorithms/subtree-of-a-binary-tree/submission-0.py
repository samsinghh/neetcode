# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            subTree = q.popleft()
            if subTree.val == subRoot.val:
                check = self.isSameTree(subTree, subRoot)
                if check:
                    return True
            
            if subTree.left:
                q.append(subTree.left)
            if subTree.right:
                q.append(subTree.right)
        
        return False