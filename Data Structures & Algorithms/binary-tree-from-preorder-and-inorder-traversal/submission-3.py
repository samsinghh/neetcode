# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
  1.           pre=[1,2,7,4,3,5,6] in=[7,2,4,1,5,3,6]
2. 3
7 4 5 6

[2, 7, 4]
[7, 2, 4]

[7]
[7]
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {v:i for i, v in enumerate(inorder)}

        curr_pre = 0

        def search(l, r):
            nonlocal curr_pre
            if l > r: 
                return None
            
            root_val = preorder[curr_pre]
            curr_pre += 1
            node = TreeNode(root_val)
            mid = inorderIndex[root_val]
            node.left = search(l, mid-1)
            node.right = search(mid+1, r)
            return node
        
        return search(0, len(preorder) - 1)