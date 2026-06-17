# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {val: index for index, val in enumerate(inorder)}

        self.index = 0

        def search(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.index]
            self.index += 1
            mid = hm[root_val]
            root = TreeNode(root_val)
            root.left = search(l, mid - 1)
            root.right = search(mid+1, r)
            return root
        
        return search(0, len(inorder) - 1)