# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root:
            if not root.left and not root.right:
                return 1
            left=self.countNodes(root.left)
            right=self.countNodes(root.right)
            return left+right+1
        