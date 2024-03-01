# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):+8gu7
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helperFunction(node,left,right):
            if not node:
                return True
            if not (left<node.val<right):
                return False
            return helperFunction(node.left,left,node.val) and helperFunction(node.right,node.val,right)
        return helperFunction(root,-float("inf"),float("inf"))

            
        