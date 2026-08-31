# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# start of preorder list will always be root node of tree
# in inorder, everything before root node val will be to the left and everything 
# after it will be to the right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        locs = {v: i for i, v in enumerate(inorder)}
        
        currIdx = 0

        def search(l, r):
            nonlocal currIdx
            if r < l:
                return None
            
            node_val = preorder[currIdx]
            currIdx += 1
            node = TreeNode(node_val)

            mid = locs[node_val]
            node.left = search(l, mid-1)
            node.right = search(mid+1, r)
            return node
        
        return search(0, len(inorder) - 1)

