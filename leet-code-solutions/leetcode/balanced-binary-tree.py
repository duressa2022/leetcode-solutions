# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0,True
            left,isleft=check(node.left)
            right,isright=check(node.right)
            height=max(left,right)+1
            balanced=isleft and isright and abs(left-right)<=1
            return height,balanced
        height,balanced=check(root)
        return balanced
        