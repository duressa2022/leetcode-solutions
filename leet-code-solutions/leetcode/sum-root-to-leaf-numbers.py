# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helperFunction(node,current):
            if not node:
                return 0
            current=current*10+node.val
            if not node.left and not node.right:
                return current
            left=helperFunction(node.left,current)
            right=helperFunction(node.right,current)
            return left+right
        return helperFunction(root,0)

        